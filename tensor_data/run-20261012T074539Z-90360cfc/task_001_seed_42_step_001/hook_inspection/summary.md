# Hook inspection: pre_action_full_prefix_replay

Status: **complete**. 731 full tensors; 950 records.

Input and output leaves are indexed separately. Call indices are local to each module. Module boundaries only; missing outputs are not reconstructed. Full values are in linked NPY files.

## Outside Transformer blocks

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | `model` | 0 | `input.kwargs['input_ids']` | [1, 174] | torch.int64 → int64 | 11.0 / 191268.0 / 15721.063218390804 / 31601.33798294141 | [NPY](tensors/0000000.npy) |
| 1 | `model` | 0 | `input.kwargs['attention_mask']` | [1, 174] | torch.int64 → int64 | 1.0 / 1.0 / 1.0 / 0.0 | [NPY](tensors/0000001.npy) |
| 2 | `model` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 3 | `model` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 4 | `model` | 0 | `input.kwargs['return_dict']` | — | bool | True | — |
| 5 | `model.embed_tokens` | 0 | `input.args[0]` | [1, 174] | torch.int64 → int64 | 11.0 / 191268.0 / 15721.063218390804 / 31601.33798294141 | [NPY](tensors/0000005.npy) |
| 6 | `model.embed_tokens` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -95.0 / 89.0 / -0.012668070864181554 / 2.9098468514672318 | [NPY](tensors/0000006.npy) |
| 7 | `model.rotary_emb` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -95.0 / 89.0 / -0.012668070864181554 / 2.9098468514672318 | [NPY](tensors/0000007.npy) |
| 8 | `model.rotary_emb` | 0 | `input.args[1]` | [1, 174] | torch.int64 → int64 | 0.0 / 173.0 / 86.5 / 50.22864388639879 | [NPY](tensors/0000008.npy) |
| 9 | `model.rotary_emb` | 0 | `output[0]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8449686751968559 / 0.8475634832262998 | [NPY](tensors/0000009.npy) |
| 10 | `model.rotary_emb` | 0 | `output[1]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11834632235160365 / 0.6025126921634434 | [NPY](tensors/0000010.npy) |
| 947 | `model.norm` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -10688.0 / 10880.0 / -0.2755838055568028 / 437.7624568706959 | [NPY](tensors/0000947.npy) |
| 948 | `model.norm` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -336.0 / 188.0 / -0.014139257373328712 / 5.788113408918075 | [NPY](tensors/0000948.npy) |
| 949 | `model` | 0 | `output['last_hidden_state']` | [1, 174, 2880] | torch.bfloat16 → float32 | -336.0 / 188.0 / -0.014139257373328712 / 5.788113408918075 | [NPY](tensors/0000949.npy) |

## Layer 0000

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 11 | `model.layers.0` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -95.0 / 89.0 / -0.012668070864181554 / 2.9098468514672318 | [NPY](tensors/0000011.npy) |
| 12 | `model.layers.0` | 0 | `input.kwargs['attention_mask']` | [1, 1, 174, 174] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.8060483674001114e+38 / 1.6911081947706832e+38 | [NPY](tensors/0000012.npy) |
| 13 | `model.layers.0` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8449686751968559 / 0.8475634832262998 | [NPY](tensors/0000013.npy) |
| 14 | `model.layers.0` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11834632235160365 / 0.6025126921634434 | [NPY](tensors/0000014.npy) |
| 15 | `model.layers.0` | 0 | `input.kwargs['position_ids']` | [1, 174] | torch.int64 → int64 | 0.0 / 173.0 / 86.5 / 50.22864388639879 | [NPY](tensors/0000015.npy) |
| 16 | `model.layers.0` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 17 | `model.layers.0` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 18 | `model.layers.0` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 19 | `model.layers.0.input_layernorm` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -95.0 / 89.0 / -0.012668070864181554 / 2.9098468514672318 | [NPY](tensors/0000019.npy) |
| 20 | `model.layers.0.input_layernorm` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.006556360355618803 / 0.7599479549643959 | [NPY](tensors/0000020.npy) |
| 21 | `model.layers.0.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 174, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.006556360355618803 / 0.7599479549643959 | [NPY](tensors/0000021.npy) |
| 22 | `model.layers.0.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 174, 174] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.8060483674001114e+38 / 1.6911081947706832e+38 | [NPY](tensors/0000022.npy) |
| 23 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 174] | torch.int64 → int64 | 0.0 / 173.0 / 86.5 / 50.22864388639879 | [NPY](tensors/0000023.npy) |
| 24 | `model.layers.0.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 25 | `model.layers.0.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 26 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8449686751968559 / 0.8475634832262998 | [NPY](tensors/0000026.npy) |
| 27 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11834632235160365 / 0.6025126921634434 | [NPY](tensors/0000027.npy) |
| 28 | `model.layers.0.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 29 | `model.layers.0.self_attn.q_proj` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.006556360355618803 / 0.7599479549643959 | [NPY](tensors/0000029.npy) |
| 30 | `model.layers.0.self_attn.q_proj` | 0 | `output` | [1, 174, 4096] | torch.bfloat16 → float32 | -8.3125 / 12.8125 / 0.02209666969257791 / 1.018507619833328 | [NPY](tensors/0000030.npy) |
| 31 | `model.layers.0.self_attn.k_proj` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.006556360355618803 / 0.7599479549643959 | [NPY](tensors/0000031.npy) |
| 32 | `model.layers.0.self_attn.k_proj` | 0 | `output` | [1, 174, 512] | torch.bfloat16 → float32 | -65.5 / 65.5 / 0.01327056943000048 / 5.847113710030833 | [NPY](tensors/0000032.npy) |
| 33 | `model.layers.0.self_attn.v_proj` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -33.5 / 15.0 / -0.006556360355618803 / 0.7599479549643959 | [NPY](tensors/0000033.npy) |
| 34 | `model.layers.0.self_attn.v_proj` | 0 | `output` | [1, 174, 512] | torch.bfloat16 → float32 | -7.375 / 7.71875 / -0.015802148087271328 / 1.1820866003157515 | [NPY](tensors/0000034.npy) |
| 35 | `model.layers.0.self_attn.o_proj` | 0 | `input.args[0]` | [1, 174, 4096] | torch.bfloat16 → float32 | -6.9375 / 7.71875 / -0.006684582129771497 / 0.5397881958202126 | [NPY](tensors/0000035.npy) |
| 36 | `model.layers.0.self_attn.o_proj` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -34.5 / 52.5 / 0.02804423343921157 / 1.1647018239136813 | [NPY](tensors/0000036.npy) |
| 37 | `model.layers.0.self_attn` | 0 | `output[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -34.5 / 52.5 / 0.02804423343921157 / 1.1647018239136813 | [NPY](tensors/0000037.npy) |
| 38 | `model.layers.0.self_attn` | 0 | `output[1]` | [1, 64, 174, 174] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0023199733776812074 / 0.031854459476315954 | [NPY](tensors/0000038.npy) |
| 39 | `model.layers.0.post_attention_layernorm` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -87.5 / 70.5 / 0.015366741630461632 / 3.028299274577275 | [NPY](tensors/0000039.npy) |
| 40 | `model.layers.0.post_attention_layernorm` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -7.21875 / 3.75 / 0.00031794485865615184 / 0.3254823826545235 | [NPY](tensors/0000040.npy) |
| 41 | `model.layers.0.mlp` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -7.21875 / 3.75 / 0.00031794485865615184 / 0.3254823826545235 | [NPY](tensors/0000041.npy) |
| 42 | `model.layers.0.mlp.experts` | 0 | `input.args[0]` | [174, 2880] | torch.bfloat16 → float32 | -7.21875 / 3.75 / 0.00031794485865615184 / 0.3254823826545235 | [NPY](tensors/0000042.npy) |
| 43 | `model.layers.0.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 44 | `model.layers.0.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 45 | `model.layers.0.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 46 | `model.layers.0.mlp.experts` | 0 | `output` | [174, 2880] | torch.bfloat16 → float32 | -50.0 / 92.5 / 0.018454872692624726 / 0.9151813241240484 | [NPY](tensors/0000046.npy) |
| 47 | `model.layers.0.mlp` | 0 | `output[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -50.0 / 92.5 / 0.018454872692624726 / 0.9151813241240484 | [NPY](tensors/0000047.npy) |
| 48 | `model.layers.0.mlp` | 0 | `output[1]` | [174, 32] | torch.bfloat16 → float32 | -4.9375 / 3.4375 / -0.10368456785706268 / 1.0446489584772665 | [NPY](tensors/0000048.npy) |
| 49 | `model.layers.0` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -89.5 / 106.0 / 0.0338145575837005 / 3.2475384679309554 | [NPY](tensors/0000049.npy) |

## Layer 0001

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 50 | `model.layers.1` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -89.5 / 106.0 / 0.0338145575837005 / 3.2475384679309554 | [NPY](tensors/0000050.npy) |
| 51 | `model.layers.1` | 0 | `input.kwargs['attention_mask']` | [1, 1, 174, 174] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6850256618980335e+38 / 1.6947377057948597e+38 | [NPY](tensors/0000051.npy) |
| 52 | `model.layers.1` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8449686751968559 / 0.8475634832262998 | [NPY](tensors/0000052.npy) |
| 53 | `model.layers.1` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11834632235160365 / 0.6025126921634434 | [NPY](tensors/0000053.npy) |
| 54 | `model.layers.1` | 0 | `input.kwargs['position_ids']` | [1, 174] | torch.int64 → int64 | 0.0 / 173.0 / 86.5 / 50.22864388639879 | [NPY](tensors/0000054.npy) |
| 55 | `model.layers.1` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 56 | `model.layers.1` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 57 | `model.layers.1` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 58 | `model.layers.1.input_layernorm` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -89.5 / 106.0 / 0.0338145575837005 / 3.2475384679309554 | [NPY](tensors/0000058.npy) |
| 59 | `model.layers.1.input_layernorm` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -28.25 / 25.625 / 0.007064817193300863 / 0.8505350828767287 | [NPY](tensors/0000059.npy) |
| 60 | `model.layers.1.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 174, 2880] | torch.bfloat16 → float32 | -28.25 / 25.625 / 0.007064817193300863 / 0.8505350828767287 | [NPY](tensors/0000060.npy) |
| 61 | `model.layers.1.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 174, 174] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6850256618980335e+38 / 1.6947377057948597e+38 | [NPY](tensors/0000061.npy) |
| 62 | `model.layers.1.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 174] | torch.int64 → int64 | 0.0 / 173.0 / 86.5 / 50.22864388639879 | [NPY](tensors/0000062.npy) |
| 63 | `model.layers.1.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 64 | `model.layers.1.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 65 | `model.layers.1.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8449686751968559 / 0.8475634832262998 | [NPY](tensors/0000065.npy) |
| 66 | `model.layers.1.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11834632235160365 / 0.6025126921634434 | [NPY](tensors/0000066.npy) |
| 67 | `model.layers.1.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 68 | `model.layers.1.self_attn.q_proj` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -28.25 / 25.625 / 0.007064817193300863 / 0.8505350828767287 | [NPY](tensors/0000068.npy) |
| 69 | `model.layers.1.self_attn.q_proj` | 0 | `output` | [1, 174, 4096] | torch.bfloat16 → float32 | -11.25 / 12.25 / -0.021553818230936536 / 1.1040224981660425 | [NPY](tensors/0000069.npy) |
| 70 | `model.layers.1.self_attn.k_proj` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -28.25 / 25.625 / 0.007064817193300863 / 0.8505350828767287 | [NPY](tensors/0000070.npy) |
| 71 | `model.layers.1.self_attn.k_proj` | 0 | `output` | [1, 174, 512] | torch.bfloat16 → float32 | -109.0 / 39.5 / -0.7128591658226375 / 7.748442905815859 | [NPY](tensors/0000071.npy) |
| 72 | `model.layers.1.self_attn.v_proj` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -28.25 / 25.625 / 0.007064817193300863 / 0.8505350828767287 | [NPY](tensors/0000072.npy) |
| 73 | `model.layers.1.self_attn.v_proj` | 0 | `output` | [1, 174, 512] | torch.bfloat16 → float32 | -6.0 / 5.84375 / 0.01473256020710386 / 0.9833853795964956 | [NPY](tensors/0000073.npy) |
| 74 | `model.layers.1.self_attn.o_proj` | 0 | `input.args[0]` | [1, 174, 4096] | torch.bfloat16 → float32 | -5.8125 / 4.9375 / 0.001677165986010571 / 0.44429369819151726 | [NPY](tensors/0000074.npy) |
| 75 | `model.layers.1.self_attn.o_proj` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -33.75 / 49.75 / 0.002934767133510216 / 0.8430887397397607 | [NPY](tensors/0000075.npy) |
| 76 | `model.layers.1.self_attn` | 0 | `output[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -33.75 / 49.75 / 0.002934767133510216 / 0.8430887397397607 | [NPY](tensors/0000076.npy) |
| 77 | `model.layers.1.self_attn` | 0 | `output[1]` | [1, 64, 174, 174] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.003824322101788299 / 0.028980344869745593 | [NPY](tensors/0000077.npy) |
| 78 | `model.layers.1.post_attention_layernorm` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -76.5 / 78.5 / 0.03675581093492179 / 3.229763060058074 | [NPY](tensors/0000078.npy) |
| 79 | `model.layers.1.post_attention_layernorm` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -4.6875 / 3.40625 / -0.00044883677693105295 / 0.35502257113423696 | [NPY](tensors/0000079.npy) |
| 80 | `model.layers.1.mlp` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -4.6875 / 3.40625 / -0.00044883677693105295 / 0.35502257113423696 | [NPY](tensors/0000080.npy) |
| 81 | `model.layers.1.mlp.experts` | 0 | `input.args[0]` | [174, 2880] | torch.bfloat16 → float32 | -4.6875 / 3.40625 / -0.00044883677693105295 / 0.35502257113423696 | [NPY](tensors/0000081.npy) |
| 82 | `model.layers.1.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 83 | `model.layers.1.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 84 | `model.layers.1.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 85 | `model.layers.1.mlp.experts` | 0 | `output` | [174, 2880] | torch.bfloat16 → float32 | -31.875 / 66.0 / 0.023857035711027045 / 1.0867731147959971 | [NPY](tensors/0000085.npy) |
| 86 | `model.layers.1.mlp` | 0 | `output[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -31.875 / 66.0 / 0.023857035711027045 / 1.0867731147959971 | [NPY](tensors/0000086.npy) |
| 87 | `model.layers.1.mlp` | 0 | `output[1]` | [174, 32] | torch.bfloat16 → float32 | -2.65625 / 2.59375 / -0.07022842319532373 / 0.7354359817955872 | [NPY](tensors/0000087.npy) |
| 88 | `model.layers.1` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -95.0 / 119.0 / 0.06061487616554835 / 3.76924989736054 | [NPY](tensors/0000088.npy) |

## Layer 0002

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 89 | `model.layers.2` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -95.0 / 119.0 / 0.06061487616554835 / 3.76924989736054 | [NPY](tensors/0000089.npy) |
| 90 | `model.layers.2` | 0 | `input.kwargs['attention_mask']` | [1, 1, 174, 174] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.8060483674001114e+38 / 1.6911081947706832e+38 | [NPY](tensors/0000090.npy) |
| 91 | `model.layers.2` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8449686751968559 / 0.8475634832262998 | [NPY](tensors/0000091.npy) |
| 92 | `model.layers.2` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11834632235160365 / 0.6025126921634434 | [NPY](tensors/0000092.npy) |
| 93 | `model.layers.2` | 0 | `input.kwargs['position_ids']` | [1, 174] | torch.int64 → int64 | 0.0 / 173.0 / 86.5 / 50.22864388639879 | [NPY](tensors/0000093.npy) |
| 94 | `model.layers.2` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 95 | `model.layers.2` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 96 | `model.layers.2` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 97 | `model.layers.2.input_layernorm` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -95.0 / 119.0 / 0.06061487616554835 / 3.76924989736054 | [NPY](tensors/0000097.npy) |
| 98 | `model.layers.2.input_layernorm` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -29.125 / 23.375 / 0.01231770043191173 / 0.8616677475727517 | [NPY](tensors/0000098.npy) |
| 99 | `model.layers.2.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 174, 2880] | torch.bfloat16 → float32 | -29.125 / 23.375 / 0.01231770043191173 / 0.8616677475727517 | [NPY](tensors/0000099.npy) |
| 100 | `model.layers.2.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 174, 174] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.8060483674001114e+38 / 1.6911081947706832e+38 | [NPY](tensors/0000100.npy) |
| 101 | `model.layers.2.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 174] | torch.int64 → int64 | 0.0 / 173.0 / 86.5 / 50.22864388639879 | [NPY](tensors/0000101.npy) |
| 102 | `model.layers.2.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 103 | `model.layers.2.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 104 | `model.layers.2.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8449686751968559 / 0.8475634832262998 | [NPY](tensors/0000104.npy) |
| 105 | `model.layers.2.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11834632235160365 / 0.6025126921634434 | [NPY](tensors/0000105.npy) |
| 106 | `model.layers.2.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 107 | `model.layers.2.self_attn.q_proj` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -29.125 / 23.375 / 0.01231770043191173 / 0.8616677475727517 | [NPY](tensors/0000107.npy) |
| 108 | `model.layers.2.self_attn.q_proj` | 0 | `output` | [1, 174, 4096] | torch.bfloat16 → float32 | -13.75 / 8.375 / 0.039259393593453554 / 0.8746229372065393 | [NPY](tensors/0000108.npy) |
| 109 | `model.layers.2.self_attn.k_proj` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -29.125 / 23.375 / 0.01231770043191173 / 0.8616677475727517 | [NPY](tensors/0000109.npy) |
| 110 | `model.layers.2.self_attn.k_proj` | 0 | `output` | [1, 174, 512] | torch.bfloat16 → float32 | -25.875 / 22.5 / -0.01803194229416121 / 2.565826416765802 | [NPY](tensors/0000110.npy) |
| 111 | `model.layers.2.self_attn.v_proj` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -29.125 / 23.375 / 0.01231770043191173 / 0.8616677475727517 | [NPY](tensors/0000111.npy) |
| 112 | `model.layers.2.self_attn.v_proj` | 0 | `output` | [1, 174, 512] | torch.bfloat16 → float32 | -8.0625 / 5.84375 / 0.023194689860289126 / 1.1666907385452234 | [NPY](tensors/0000112.npy) |
| 113 | `model.layers.2.self_attn.o_proj` | 0 | `input.args[0]` | [1, 174, 4096] | torch.bfloat16 → float32 | -6.5 / 4.71875 / 0.013703689480280444 / 0.47597034353362244 | [NPY](tensors/0000113.npy) |
| 114 | `model.layers.2.self_attn.o_proj` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -41.25 / 52.0 / 0.001578390487992487 / 0.9968715959485813 | [NPY](tensors/0000114.npy) |
| 115 | `model.layers.2.self_attn` | 0 | `output[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -41.25 / 52.0 / 0.001578390487992487 / 0.9968715959485813 | [NPY](tensors/0000115.npy) |
| 116 | `model.layers.2.self_attn` | 0 | `output[1]` | [1, 64, 174, 174] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0027986048662132254 / 0.02388586881818574 | [NPY](tensors/0000116.npy) |
| 117 | `model.layers.2.post_attention_layernorm` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -84.0 / 123.5 / 0.06219859809863309 / 3.7272757851410225 | [NPY](tensors/0000117.npy) |
| 118 | `model.layers.2.post_attention_layernorm` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -5.84375 / 4.21875 / 0.0014421219678207907 / 0.45424451338402405 | [NPY](tensors/0000118.npy) |
| 119 | `model.layers.2.mlp` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -5.84375 / 4.21875 / 0.0014421219678207907 / 0.45424451338402405 | [NPY](tensors/0000119.npy) |
| 120 | `model.layers.2.mlp.experts` | 0 | `input.args[0]` | [174, 2880] | torch.bfloat16 → float32 | -5.84375 / 4.21875 / 0.0014421219678207907 / 0.45424451338402405 | [NPY](tensors/0000120.npy) |
| 121 | `model.layers.2.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 122 | `model.layers.2.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 123 | `model.layers.2.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 124 | `model.layers.2.mlp.experts` | 0 | `output` | [174, 2880] | torch.bfloat16 → float32 | -45.25 / 88.0 / 0.032424237940217794 / 1.382412689879989 | [NPY](tensors/0000124.npy) |
| 125 | `model.layers.2.mlp` | 0 | `output[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -45.25 / 88.0 / 0.032424237940217794 / 1.382412689879989 | [NPY](tensors/0000125.npy) |
| 126 | `model.layers.2.mlp` | 0 | `output[1]` | [174, 32] | torch.bfloat16 → float32 | -3.09375 / 2.21875 / -0.08893874595905173 / 0.6633861192453863 | [NPY](tensors/0000126.npy) |
| 127 | `model.layers.2` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -100.5 / 148.0 / 0.09463078442813488 / 4.493880608361403 | [NPY](tensors/0000127.npy) |

## Layer 0003

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 128 | `model.layers.3` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -100.5 / 148.0 / 0.09463078442813488 / 4.493880608361403 | [NPY](tensors/0000128.npy) |
| 129 | `model.layers.3` | 0 | `input.kwargs['attention_mask']` | [1, 1, 174, 174] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6850256618980335e+38 / 1.6947377057948597e+38 | [NPY](tensors/0000129.npy) |
| 130 | `model.layers.3` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8449686751968559 / 0.8475634832262998 | [NPY](tensors/0000130.npy) |
| 131 | `model.layers.3` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11834632235160365 / 0.6025126921634434 | [NPY](tensors/0000131.npy) |
| 132 | `model.layers.3` | 0 | `input.kwargs['position_ids']` | [1, 174] | torch.int64 → int64 | 0.0 / 173.0 / 86.5 / 50.22864388639879 | [NPY](tensors/0000132.npy) |
| 133 | `model.layers.3` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 134 | `model.layers.3` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 135 | `model.layers.3` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 136 | `model.layers.3.input_layernorm` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -100.5 / 148.0 / 0.09463078442813488 / 4.493880608361403 | [NPY](tensors/0000136.npy) |
| 137 | `model.layers.3.input_layernorm` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -53.5 / 56.75 / 0.035309046874177255 / 1.275743257132619 | [NPY](tensors/0000137.npy) |
| 138 | `model.layers.3.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 174, 2880] | torch.bfloat16 → float32 | -53.5 / 56.75 / 0.035309046874177255 / 1.275743257132619 | [NPY](tensors/0000138.npy) |
| 139 | `model.layers.3.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 174, 174] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6850256618980335e+38 / 1.6947377057948597e+38 | [NPY](tensors/0000139.npy) |
| 140 | `model.layers.3.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 174] | torch.int64 → int64 | 0.0 / 173.0 / 86.5 / 50.22864388639879 | [NPY](tensors/0000140.npy) |
| 141 | `model.layers.3.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 142 | `model.layers.3.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 143 | `model.layers.3.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8449686751968559 / 0.8475634832262998 | [NPY](tensors/0000143.npy) |
| 144 | `model.layers.3.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11834632235160365 / 0.6025126921634434 | [NPY](tensors/0000144.npy) |
| 145 | `model.layers.3.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 146 | `model.layers.3.self_attn.q_proj` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -53.5 / 56.75 / 0.035309046874177255 / 1.275743257132619 | [NPY](tensors/0000146.npy) |
| 147 | `model.layers.3.self_attn.q_proj` | 0 | `output` | [1, 174, 4096] | torch.bfloat16 → float32 | -12.5625 / 9.0 / -0.024534801693888945 / 1.1048580551680993 | [NPY](tensors/0000147.npy) |
| 148 | `model.layers.3.self_attn.k_proj` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -53.5 / 56.75 / 0.035309046874177255 / 1.275743257132619 | [NPY](tensors/0000148.npy) |
| 149 | `model.layers.3.self_attn.k_proj` | 0 | `output` | [1, 174, 512] | torch.bfloat16 → float32 | -78.5 / 56.75 / -0.07173084202169001 / 4.840858960056053 | [NPY](tensors/0000149.npy) |
| 150 | `model.layers.3.self_attn.v_proj` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -53.5 / 56.75 / 0.035309046874177255 / 1.275743257132619 | [NPY](tensors/0000150.npy) |
| 151 | `model.layers.3.self_attn.v_proj` | 0 | `output` | [1, 174, 512] | torch.bfloat16 → float32 | -7.5 / 11.4375 / 0.019502005786046214 / 0.967295225767016 | [NPY](tensors/0000151.npy) |
| 152 | `model.layers.3.self_attn.o_proj` | 0 | `input.args[0]` | [1, 174, 4096] | torch.bfloat16 → float32 | -3.671875 / 3.203125 / 0.009129902701684402 / 0.31435623262377105 | [NPY](tensors/0000152.npy) |
| 153 | `model.layers.3.self_attn.o_proj` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -62.75 / 34.5 / -0.007126032491006422 / 1.0428393169688273 | [NPY](tensors/0000153.npy) |
| 154 | `model.layers.3.self_attn` | 0 | `output[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -62.75 / 34.5 / -0.007126032491006422 / 1.0428393169688273 | [NPY](tensors/0000154.npy) |
| 155 | `model.layers.3.self_attn` | 0 | `output[1]` | [1, 64, 174, 174] | torch.bfloat16 → float32 | 0.0 / 0.9765625 / 0.0027832535137005806 / 0.01654686254514564 | [NPY](tensors/0000155.npy) |
| 156 | `model.layers.3.post_attention_layernorm` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -103.0 / 134.0 / 0.08750085225079024 / 4.416606687870551 | [NPY](tensors/0000156.npy) |
| 157 | `model.layers.3.post_attention_layernorm` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -6.0 / 5.75 / 0.004532351402392181 / 0.5169278370185098 | [NPY](tensors/0000157.npy) |
| 158 | `model.layers.3.mlp` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -6.0 / 5.75 / 0.004532351402392181 / 0.5169278370185098 | [NPY](tensors/0000158.npy) |
| 159 | `model.layers.3.mlp.experts` | 0 | `input.args[0]` | [174, 2880] | torch.bfloat16 → float32 | -6.0 / 5.75 / 0.004532351402392181 / 0.5169278370185098 | [NPY](tensors/0000159.npy) |
| 160 | `model.layers.3.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 161 | `model.layers.3.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 162 | `model.layers.3.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 163 | `model.layers.3.mlp.experts` | 0 | `output` | [174, 2880] | torch.bfloat16 → float32 | -61.25 / 93.0 / 0.025977135541947558 / 1.5074742852886711 | [NPY](tensors/0000163.npy) |
| 164 | `model.layers.3.mlp` | 0 | `output[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -61.25 / 93.0 / 0.025977135541947558 / 1.5074742852886711 | [NPY](tensors/0000164.npy) |
| 165 | `model.layers.3.mlp` | 0 | `output[1]` | [174, 32] | torch.bfloat16 → float32 | -3.234375 / 1.828125 / -0.06931316441503065 / 0.5399992998087285 | [NPY](tensors/0000165.npy) |
| 166 | `model.layers.3` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -149.0 / 172.0 / 0.11346706022552451 / 5.298443517591344 | [NPY](tensors/0000166.npy) |

## Layer 0004

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 167 | `model.layers.4` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -149.0 / 172.0 / 0.11346706022552451 / 5.298443517591344 | [NPY](tensors/0000167.npy) |
| 168 | `model.layers.4` | 0 | `input.kwargs['attention_mask']` | [1, 1, 174, 174] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.8060483674001114e+38 / 1.6911081947706832e+38 | [NPY](tensors/0000168.npy) |
| 169 | `model.layers.4` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8449686751968559 / 0.8475634832262998 | [NPY](tensors/0000169.npy) |
| 170 | `model.layers.4` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11834632235160365 / 0.6025126921634434 | [NPY](tensors/0000170.npy) |
| 171 | `model.layers.4` | 0 | `input.kwargs['position_ids']` | [1, 174] | torch.int64 → int64 | 0.0 / 173.0 / 86.5 / 50.22864388639879 | [NPY](tensors/0000171.npy) |
| 172 | `model.layers.4` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 173 | `model.layers.4` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 174 | `model.layers.4` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 175 | `model.layers.4.input_layernorm` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -149.0 / 172.0 / 0.11346706022552451 / 5.298443517591344 | [NPY](tensors/0000175.npy) |
| 176 | `model.layers.4.input_layernorm` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -38.75 / 33.25 / 0.02055865879649936 / 1.1442516423322433 | [NPY](tensors/0000176.npy) |
| 177 | `model.layers.4.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 174, 2880] | torch.bfloat16 → float32 | -38.75 / 33.25 / 0.02055865879649936 / 1.1442516423322433 | [NPY](tensors/0000177.npy) |
| 178 | `model.layers.4.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 174, 174] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.8060483674001114e+38 / 1.6911081947706832e+38 | [NPY](tensors/0000178.npy) |
| 179 | `model.layers.4.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 174] | torch.int64 → int64 | 0.0 / 173.0 / 86.5 / 50.22864388639879 | [NPY](tensors/0000179.npy) |
| 180 | `model.layers.4.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 181 | `model.layers.4.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 182 | `model.layers.4.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8449686751968559 / 0.8475634832262998 | [NPY](tensors/0000182.npy) |
| 183 | `model.layers.4.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11834632235160365 / 0.6025126921634434 | [NPY](tensors/0000183.npy) |
| 184 | `model.layers.4.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 185 | `model.layers.4.self_attn.q_proj` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -38.75 / 33.25 / 0.02055865879649936 / 1.1442516423322433 | [NPY](tensors/0000185.npy) |
| 186 | `model.layers.4.self_attn.q_proj` | 0 | `output` | [1, 174, 4096] | torch.bfloat16 → float32 | -16.75 / 7.59375 / -0.009449850112335182 / 1.0309942852418081 | [NPY](tensors/0000186.npy) |
| 187 | `model.layers.4.self_attn.k_proj` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -38.75 / 33.25 / 0.02055865879649936 / 1.1442516423322433 | [NPY](tensors/0000187.npy) |
| 188 | `model.layers.4.self_attn.k_proj` | 0 | `output` | [1, 174, 512] | torch.bfloat16 → float32 | -12.5625 / 99.0 / 0.23160958778241586 / 4.329044512907715 | [NPY](tensors/0000188.npy) |
| 189 | `model.layers.4.self_attn.v_proj` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -38.75 / 33.25 / 0.02055865879649936 / 1.1442516423322433 | [NPY](tensors/0000189.npy) |
| 190 | `model.layers.4.self_attn.v_proj` | 0 | `output` | [1, 174, 512] | torch.bfloat16 → float32 | -10.8125 / 16.25 / 0.0024686191958942635 / 1.3434326139845172 | [NPY](tensors/0000190.npy) |
| 191 | `model.layers.4.self_attn.o_proj` | 0 | `input.args[0]` | [1, 174, 4096] | torch.bfloat16 → float32 | -9.625 / 15.0625 / -0.005566782648115961 / 0.5903774212328925 | [NPY](tensors/0000191.npy) |
| 192 | `model.layers.4.self_attn.o_proj` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -69.0 / 44.0 / -0.0071637833411573384 / 1.2907850062638093 | [NPY](tensors/0000192.npy) |
| 193 | `model.layers.4.self_attn` | 0 | `output[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -69.0 / 44.0 / -0.0071637833411573384 / 1.2907850062638093 | [NPY](tensors/0000193.npy) |
| 194 | `model.layers.4.self_attn` | 0 | `output[1]` | [1, 64, 174, 174] | torch.bfloat16 → float32 | 0.0 / 0.98046875 / 0.0028863214166559683 / 0.02318860235833807 | [NPY](tensors/0000194.npy) |
| 195 | `model.layers.4.post_attention_layernorm` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -135.0 / 149.0 / 0.10630497782470927 / 5.220565453402402 | [NPY](tensors/0000195.npy) |
| 196 | `model.layers.4.post_attention_layernorm` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -5.59375 / 6.90625 / 0.006512510060959544 / 0.5802416816970152 | [NPY](tensors/0000196.npy) |
| 197 | `model.layers.4.mlp` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -5.59375 / 6.90625 / 0.006512510060959544 / 0.5802416816970152 | [NPY](tensors/0000197.npy) |
| 198 | `model.layers.4.mlp.experts` | 0 | `input.args[0]` | [174, 2880] | torch.bfloat16 → float32 | -5.59375 / 6.90625 / 0.006512510060959544 / 0.5802416816970152 | [NPY](tensors/0000198.npy) |
| 199 | `model.layers.4.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 200 | `model.layers.4.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 201 | `model.layers.4.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 202 | `model.layers.4.mlp.experts` | 0 | `output` | [174, 2880] | torch.bfloat16 → float32 | -81.5 / 164.0 / 0.05513255298137665 / 2.5602708848214673 | [NPY](tensors/0000202.npy) |
| 203 | `model.layers.4.mlp` | 0 | `output[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -81.5 / 164.0 / 0.05513255298137665 / 2.5602708848214673 | [NPY](tensors/0000203.npy) |
| 204 | `model.layers.4.mlp` | 0 | `output[1]` | [174, 32] | torch.bfloat16 → float32 | -3.109375 / 2.171875 / -0.07986424435144183 / 0.5987428611395048 | [NPY](tensors/0000204.npy) |
| 205 | `model.layers.4` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -191.0 / 253.0 / 0.16144712297091238 / 6.8607744801548565 | [NPY](tensors/0000205.npy) |

## Layer 0005

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 206 | `model.layers.5` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -191.0 / 253.0 / 0.16144712297091238 / 6.8607744801548565 | [NPY](tensors/0000206.npy) |
| 207 | `model.layers.5` | 0 | `input.kwargs['attention_mask']` | [1, 1, 174, 174] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6850256618980335e+38 / 1.6947377057948597e+38 | [NPY](tensors/0000207.npy) |
| 208 | `model.layers.5` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8449686751968559 / 0.8475634832262998 | [NPY](tensors/0000208.npy) |
| 209 | `model.layers.5` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11834632235160365 / 0.6025126921634434 | [NPY](tensors/0000209.npy) |
| 210 | `model.layers.5` | 0 | `input.kwargs['position_ids']` | [1, 174] | torch.int64 → int64 | 0.0 / 173.0 / 86.5 / 50.22864388639879 | [NPY](tensors/0000210.npy) |
| 211 | `model.layers.5` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 212 | `model.layers.5` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 213 | `model.layers.5` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 214 | `model.layers.5.input_layernorm` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -191.0 / 253.0 / 0.16144712297091238 / 6.8607744801548565 | [NPY](tensors/0000214.npy) |
| 215 | `model.layers.5.input_layernorm` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -28.25 / 41.0 / 0.0336854067603709 / 1.1865744970301622 | [NPY](tensors/0000215.npy) |
| 216 | `model.layers.5.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 174, 2880] | torch.bfloat16 → float32 | -28.25 / 41.0 / 0.0336854067603709 / 1.1865744970301622 | [NPY](tensors/0000216.npy) |
| 217 | `model.layers.5.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 174, 174] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6850256618980335e+38 / 1.6947377057948597e+38 | [NPY](tensors/0000217.npy) |
| 218 | `model.layers.5.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 174] | torch.int64 → int64 | 0.0 / 173.0 / 86.5 / 50.22864388639879 | [NPY](tensors/0000218.npy) |
| 219 | `model.layers.5.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 220 | `model.layers.5.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 221 | `model.layers.5.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8449686751968559 / 0.8475634832262998 | [NPY](tensors/0000221.npy) |
| 222 | `model.layers.5.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11834632235160365 / 0.6025126921634434 | [NPY](tensors/0000222.npy) |
| 223 | `model.layers.5.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 224 | `model.layers.5.self_attn.q_proj` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -28.25 / 41.0 / 0.0336854067603709 / 1.1865744970301622 | [NPY](tensors/0000224.npy) |
| 225 | `model.layers.5.self_attn.q_proj` | 0 | `output` | [1, 174, 4096] | torch.bfloat16 → float32 | -18.75 / 15.0 / -0.056379623023248907 / 1.402178193894168 | [NPY](tensors/0000225.npy) |
| 226 | `model.layers.5.self_attn.k_proj` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -28.25 / 41.0 / 0.0336854067603709 / 1.1865744970301622 | [NPY](tensors/0000226.npy) |
| 227 | `model.layers.5.self_attn.k_proj` | 0 | `output` | [1, 174, 512] | torch.bfloat16 → float32 | -35.25 / 39.75 / -0.03975453214912579 / 3.4310550467877494 | [NPY](tensors/0000227.npy) |
| 228 | `model.layers.5.self_attn.v_proj` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -28.25 / 41.0 / 0.0336854067603709 / 1.1865744970301622 | [NPY](tensors/0000228.npy) |
| 229 | `model.layers.5.self_attn.v_proj` | 0 | `output` | [1, 174, 512] | torch.bfloat16 → float32 | -7.28125 / 8.375 / 0.008721484021208752 / 1.1993786845034122 | [NPY](tensors/0000229.npy) |
| 230 | `model.layers.5.self_attn.o_proj` | 0 | `input.args[0]` | [1, 174, 4096] | torch.bfloat16 → float32 | -4.3125 / 5.5 / 0.0117868501747433 / 0.5139465174713868 | [NPY](tensors/0000230.npy) |
| 231 | `model.layers.5.self_attn.o_proj` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -69.5 / 63.25 / -0.00872715857821977 / 1.4725242789473791 | [NPY](tensors/0000231.npy) |
| 232 | `model.layers.5.self_attn` | 0 | `output[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -69.5 / 63.25 / -0.00872715857821977 / 1.4725242789473791 | [NPY](tensors/0000232.npy) |
| 233 | `model.layers.5.self_attn` | 0 | `output[1]` | [1, 64, 174, 174] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.003059145780804774 / 0.01872962848895955 | [NPY](tensors/0000233.npy) |
| 234 | `model.layers.5.post_attention_layernorm` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -130.0 / 208.0 / 0.1527006926968941 / 7.0658112351100675 | [NPY](tensors/0000234.npy) |
| 235 | `model.layers.5.post_attention_layernorm` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -5.59375 / 5.6875 / 0.00641426579125159 / 0.5661805778301803 | [NPY](tensors/0000235.npy) |
| 236 | `model.layers.5.mlp` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -5.59375 / 5.6875 / 0.00641426579125159 / 0.5661805778301803 | [NPY](tensors/0000236.npy) |
| 237 | `model.layers.5.mlp.experts` | 0 | `input.args[0]` | [174, 2880] | torch.bfloat16 → float32 | -5.59375 / 5.6875 / 0.00641426579125159 / 0.5661805778301803 | [NPY](tensors/0000237.npy) |
| 238 | `model.layers.5.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 239 | `model.layers.5.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 240 | `model.layers.5.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 241 | `model.layers.5.mlp.experts` | 0 | `output` | [174, 2880] | torch.bfloat16 → float32 | -123.0 / 118.5 / 0.0401944479494716 / 2.676615811206327 | [NPY](tensors/0000241.npy) |
| 242 | `model.layers.5.mlp` | 0 | `output[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -123.0 / 118.5 / 0.0401944479494716 / 2.676615811206327 | [NPY](tensors/0000242.npy) |
| 243 | `model.layers.5.mlp` | 0 | `output[1]` | [174, 32] | torch.bfloat16 → float32 | -3.5625 / 2.265625 / -0.0890258345110663 / 0.5851495214483861 | [NPY](tensors/0000243.npy) |
| 244 | `model.layers.5` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -195.0 / 296.0 / 0.1929038095291547 / 8.709322513549976 | [NPY](tensors/0000244.npy) |

## Layer 0006

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 245 | `model.layers.6` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -195.0 / 296.0 / 0.1929038095291547 / 8.709322513549976 | [NPY](tensors/0000245.npy) |
| 246 | `model.layers.6` | 0 | `input.kwargs['attention_mask']` | [1, 1, 174, 174] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.8060483674001114e+38 / 1.6911081947706832e+38 | [NPY](tensors/0000246.npy) |
| 247 | `model.layers.6` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8449686751968559 / 0.8475634832262998 | [NPY](tensors/0000247.npy) |
| 248 | `model.layers.6` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11834632235160365 / 0.6025126921634434 | [NPY](tensors/0000248.npy) |
| 249 | `model.layers.6` | 0 | `input.kwargs['position_ids']` | [1, 174] | torch.int64 → int64 | 0.0 / 173.0 / 86.5 / 50.22864388639879 | [NPY](tensors/0000249.npy) |
| 250 | `model.layers.6` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 251 | `model.layers.6` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 252 | `model.layers.6` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 253 | `model.layers.6.input_layernorm` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -195.0 / 296.0 / 0.1929038095291547 / 8.709322513549976 | [NPY](tensors/0000253.npy) |
| 254 | `model.layers.6.input_layernorm` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -30.25 / 43.0 / 0.029566075720873067 / 1.3129798599314408 | [NPY](tensors/0000254.npy) |
| 255 | `model.layers.6.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 174, 2880] | torch.bfloat16 → float32 | -30.25 / 43.0 / 0.029566075720873067 / 1.3129798599314408 | [NPY](tensors/0000255.npy) |
| 256 | `model.layers.6.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 174, 174] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.8060483674001114e+38 / 1.6911081947706832e+38 | [NPY](tensors/0000256.npy) |
| 257 | `model.layers.6.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 174] | torch.int64 → int64 | 0.0 / 173.0 / 86.5 / 50.22864388639879 | [NPY](tensors/0000257.npy) |
| 258 | `model.layers.6.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 259 | `model.layers.6.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 260 | `model.layers.6.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8449686751968559 / 0.8475634832262998 | [NPY](tensors/0000260.npy) |
| 261 | `model.layers.6.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11834632235160365 / 0.6025126921634434 | [NPY](tensors/0000261.npy) |
| 262 | `model.layers.6.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 263 | `model.layers.6.self_attn.q_proj` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -30.25 / 43.0 / 0.029566075720873067 / 1.3129798599314408 | [NPY](tensors/0000263.npy) |
| 264 | `model.layers.6.self_attn.q_proj` | 0 | `output` | [1, 174, 4096] | torch.bfloat16 → float32 | -29.0 / 16.625 / -0.026303298527490443 / 1.1610460171384795 | [NPY](tensors/0000264.npy) |
| 265 | `model.layers.6.self_attn.k_proj` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -30.25 / 43.0 / 0.029566075720873067 / 1.3129798599314408 | [NPY](tensors/0000265.npy) |
| 266 | `model.layers.6.self_attn.k_proj` | 0 | `output` | [1, 174, 512] | torch.bfloat16 → float32 | -19.5 / 32.5 / 0.2084052188685913 / 2.378442305027613 | [NPY](tensors/0000266.npy) |
| 267 | `model.layers.6.self_attn.v_proj` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -30.25 / 43.0 / 0.029566075720873067 / 1.3129798599314408 | [NPY](tensors/0000267.npy) |
| 268 | `model.layers.6.self_attn.v_proj` | 0 | `output` | [1, 174, 512] | torch.bfloat16 → float32 | -7.59375 / 8.1875 / -0.054507248017979765 / 1.6490058170956323 | [NPY](tensors/0000268.npy) |
| 269 | `model.layers.6.self_attn.o_proj` | 0 | `input.args[0]` | [1, 174, 4096] | torch.bfloat16 → float32 | -7.03125 / 7.6875 / -0.03405266765313125 / 0.8270693214099772 | [NPY](tensors/0000269.npy) |
| 270 | `model.layers.6.self_attn.o_proj` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -91.0 / 82.0 / -0.0037203799461586686 / 1.960860587379708 | [NPY](tensors/0000270.npy) |
| 271 | `model.layers.6.self_attn` | 0 | `output[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -91.0 / 82.0 / -0.0037203799461586686 / 1.960860587379708 | [NPY](tensors/0000271.npy) |
| 272 | `model.layers.6.self_attn` | 0 | `output[1]` | [1, 64, 174, 174] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0031371363043395267 / 0.026626038808316828 | [NPY](tensors/0000272.npy) |
| 273 | `model.layers.6.post_attention_layernorm` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -179.0 / 247.0 / 0.18915475346576208 / 8.601503140884285 | [NPY](tensors/0000273.npy) |
| 274 | `model.layers.6.post_attention_layernorm` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -22.0 / 4.875 / 0.010323788764224047 / 0.6127529241579358 | [NPY](tensors/0000274.npy) |
| 275 | `model.layers.6.mlp` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -22.0 / 4.875 / 0.010323788764224047 / 0.6127529241579358 | [NPY](tensors/0000275.npy) |
| 276 | `model.layers.6.mlp.experts` | 0 | `input.args[0]` | [174, 2880] | torch.bfloat16 → float32 | -22.0 / 4.875 / 0.010323788764224047 / 0.6127529241579358 | [NPY](tensors/0000276.npy) |
| 277 | `model.layers.6.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 278 | `model.layers.6.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 279 | `model.layers.6.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 280 | `model.layers.6.mlp.experts` | 0 | `output` | [174, 2880] | torch.bfloat16 → float32 | -41472.0 / 968.0 / -0.051392706041135085 / 58.76375343873515 | [NPY](tensors/0000280.npy) |
| 281 | `model.layers.6.mlp` | 0 | `output[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -41472.0 / 968.0 / -0.051392706041135085 / 58.76375343873515 | [NPY](tensors/0000281.npy) |
| 282 | `model.layers.6.mlp` | 0 | `output[1]` | [174, 32] | torch.bfloat16 → float32 | -3.59375 / 5.0 / -0.10010684221640401 / 0.7406610069576949 | [NPY](tensors/0000282.npy) |
| 283 | `model.layers.6` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -41472.0 / 1080.0 / 0.1380102767798179 / 59.64553160334324 | [NPY](tensors/0000283.npy) |

## Layer 0007

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 284 | `model.layers.7` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -41472.0 / 1080.0 / 0.1380102767798179 / 59.64553160334324 | [NPY](tensors/0000284.npy) |
| 285 | `model.layers.7` | 0 | `input.kwargs['attention_mask']` | [1, 1, 174, 174] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6850256618980335e+38 / 1.6947377057948597e+38 | [NPY](tensors/0000285.npy) |
| 286 | `model.layers.7` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8449686751968559 / 0.8475634832262998 | [NPY](tensors/0000286.npy) |
| 287 | `model.layers.7` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11834632235160365 / 0.6025126921634434 | [NPY](tensors/0000287.npy) |
| 288 | `model.layers.7` | 0 | `input.kwargs['position_ids']` | [1, 174] | torch.int64 → int64 | 0.0 / 173.0 / 86.5 / 50.22864388639879 | [NPY](tensors/0000288.npy) |
| 289 | `model.layers.7` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 290 | `model.layers.7` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 291 | `model.layers.7` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 292 | `model.layers.7.input_layernorm` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -41472.0 / 1080.0 / 0.1380102767798179 / 59.64553160334324 | [NPY](tensors/0000292.npy) |
| 293 | `model.layers.7.input_layernorm` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -194.0 / 59.75 / 0.03467840818803648 / 1.6373850946457869 | [NPY](tensors/0000293.npy) |
| 294 | `model.layers.7.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 174, 2880] | torch.bfloat16 → float32 | -194.0 / 59.75 / 0.03467840818803648 / 1.6373850946457869 | [NPY](tensors/0000294.npy) |
| 295 | `model.layers.7.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 174, 174] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6850256618980335e+38 / 1.6947377057948597e+38 | [NPY](tensors/0000295.npy) |
| 296 | `model.layers.7.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 174] | torch.int64 → int64 | 0.0 / 173.0 / 86.5 / 50.22864388639879 | [NPY](tensors/0000296.npy) |
| 297 | `model.layers.7.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 298 | `model.layers.7.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 299 | `model.layers.7.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8449686751968559 / 0.8475634832262998 | [NPY](tensors/0000299.npy) |
| 300 | `model.layers.7.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11834632235160365 / 0.6025126921634434 | [NPY](tensors/0000300.npy) |
| 301 | `model.layers.7.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 302 | `model.layers.7.self_attn.q_proj` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -194.0 / 59.75 / 0.03467840818803648 / 1.6373850946457869 | [NPY](tensors/0000302.npy) |
| 303 | `model.layers.7.self_attn.q_proj` | 0 | `output` | [1, 174, 4096] | torch.bfloat16 → float32 | -13.4375 / 13.1875 / -0.12177626046223881 / 1.4190853081703754 | [NPY](tensors/0000303.npy) |
| 304 | `model.layers.7.self_attn.k_proj` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -194.0 / 59.75 / 0.03467840818803648 / 1.6373850946457869 | [NPY](tensors/0000304.npy) |
| 305 | `model.layers.7.self_attn.k_proj` | 0 | `output` | [1, 174, 512] | torch.bfloat16 → float32 | -129.0 / 33.75 / -0.08273441267424617 / 5.402940187119558 | [NPY](tensors/0000305.npy) |
| 306 | `model.layers.7.self_attn.v_proj` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -194.0 / 59.75 / 0.03467840818803648 / 1.6373850946457869 | [NPY](tensors/0000306.npy) |
| 307 | `model.layers.7.self_attn.v_proj` | 0 | `output` | [1, 174, 512] | torch.bfloat16 → float32 | -17.0 / 10.75 / 0.01487718702390276 / 1.6658877594278736 | [NPY](tensors/0000307.npy) |
| 308 | `model.layers.7.self_attn.o_proj` | 0 | `input.args[0]` | [1, 174, 4096] | torch.bfloat16 → float32 | -7.6875 / 7.84375 / -0.0017686778012989896 / 0.8917119497282381 | [NPY](tensors/0000308.npy) |
| 309 | `model.layers.7.self_attn.o_proj` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -120.0 / 122.0 / -0.005895336893402601 / 2.337716475928555 | [NPY](tensors/0000309.npy) |
| 310 | `model.layers.7.self_attn` | 0 | `output[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -120.0 / 122.0 / -0.005895336893402601 / 2.337716475928555 | [NPY](tensors/0000310.npy) |
| 311 | `model.layers.7.self_attn` | 0 | `output[1]` | [1, 64, 174, 174] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.004303758114370602 / 0.030641644642313844 | [NPY](tensors/0000311.npy) |
| 312 | `model.layers.7.post_attention_layernorm` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -41472.0 / 1104.0 / 0.132129772199677 / 59.62736899820511 | [NPY](tensors/0000312.npy) |
| 313 | `model.layers.7.post_attention_layernorm` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -77.0 / 5.375 / 0.008402241081579817 / 0.6345604356185132 | [NPY](tensors/0000313.npy) |
| 314 | `model.layers.7.mlp` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -77.0 / 5.375 / 0.008402241081579817 / 0.6345604356185132 | [NPY](tensors/0000314.npy) |
| 315 | `model.layers.7.mlp.experts` | 0 | `input.args[0]` | [174, 2880] | torch.bfloat16 → float32 | -77.0 / 5.375 / 0.008402241081579817 / 0.6345604356185132 | [NPY](tensors/0000315.npy) |
| 316 | `model.layers.7.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 317 | `model.layers.7.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 318 | `model.layers.7.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 319 | `model.layers.7.mlp.experts` | 0 | `output` | [174, 2880] | torch.bfloat16 → float32 | -158.0 / 166.0 / 0.032751634545709896 / 3.554343892146713 | [NPY](tensors/0000319.npy) |
| 320 | `model.layers.7.mlp` | 0 | `output[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -158.0 / 166.0 / 0.032751634545709896 / 3.554343892146713 | [NPY](tensors/0000320.npy) |
| 321 | `model.layers.7.mlp` | 0 | `output[1]` | [174, 32] | torch.bfloat16 → float32 | -3.890625 / 3.828125 / -0.1215952895153528 / 0.7994253929495903 | [NPY](tensors/0000321.npy) |
| 322 | `model.layers.7` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -41472.0 / 1128.0 / 0.16491662234943336 / 60.0414766773512 | [NPY](tensors/0000322.npy) |

## Layer 0008

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 323 | `model.layers.8` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -41472.0 / 1128.0 / 0.16491662234943336 / 60.0414766773512 | [NPY](tensors/0000323.npy) |
| 324 | `model.layers.8` | 0 | `input.kwargs['attention_mask']` | [1, 1, 174, 174] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.8060483674001114e+38 / 1.6911081947706832e+38 | [NPY](tensors/0000324.npy) |
| 325 | `model.layers.8` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8449686751968559 / 0.8475634832262998 | [NPY](tensors/0000325.npy) |
| 326 | `model.layers.8` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11834632235160365 / 0.6025126921634434 | [NPY](tensors/0000326.npy) |
| 327 | `model.layers.8` | 0 | `input.kwargs['position_ids']` | [1, 174] | torch.int64 → int64 | 0.0 / 173.0 / 86.5 / 50.22864388639879 | [NPY](tensors/0000327.npy) |
| 328 | `model.layers.8` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 329 | `model.layers.8` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 330 | `model.layers.8` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 331 | `model.layers.8.input_layernorm` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -41472.0 / 1128.0 / 0.16491662234943336 / 60.0414766773512 | [NPY](tensors/0000331.npy) |
| 332 | `model.layers.8.input_layernorm` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -121.5 / 43.25 / 0.025893470052377552 / 1.331772375396543 | [NPY](tensors/0000332.npy) |
| 333 | `model.layers.8.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 174, 2880] | torch.bfloat16 → float32 | -121.5 / 43.25 / 0.025893470052377552 / 1.331772375396543 | [NPY](tensors/0000333.npy) |
| 334 | `model.layers.8.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 174, 174] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.8060483674001114e+38 / 1.6911081947706832e+38 | [NPY](tensors/0000334.npy) |
| 335 | `model.layers.8.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 174] | torch.int64 → int64 | 0.0 / 173.0 / 86.5 / 50.22864388639879 | [NPY](tensors/0000335.npy) |
| 336 | `model.layers.8.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 337 | `model.layers.8.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 338 | `model.layers.8.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8449686751968559 / 0.8475634832262998 | [NPY](tensors/0000338.npy) |
| 339 | `model.layers.8.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11834632235160365 / 0.6025126921634434 | [NPY](tensors/0000339.npy) |
| 340 | `model.layers.8.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 341 | `model.layers.8.self_attn.q_proj` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -121.5 / 43.25 / 0.025893470052377552 / 1.331772375396543 | [NPY](tensors/0000341.npy) |
| 342 | `model.layers.8.self_attn.q_proj` | 0 | `output` | [1, 174, 4096] | torch.bfloat16 → float32 | -14.875 / 15.25 / -0.00916181787117197 / 1.0573003449365093 | [NPY](tensors/0000342.npy) |
| 343 | `model.layers.8.self_attn.k_proj` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -121.5 / 43.25 / 0.025893470052377552 / 1.331772375396543 | [NPY](tensors/0000343.npy) |
| 344 | `model.layers.8.self_attn.k_proj` | 0 | `output` | [1, 174, 512] | torch.bfloat16 → float32 | -22.375 / 28.875 / -0.00048791337356870546 / 2.2297505728196216 | [NPY](tensors/0000344.npy) |
| 345 | `model.layers.8.self_attn.v_proj` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -121.5 / 43.25 / 0.025893470052377552 / 1.331772375396543 | [NPY](tensors/0000345.npy) |
| 346 | `model.layers.8.self_attn.v_proj` | 0 | `output` | [1, 174, 512] | torch.bfloat16 → float32 | -9.375 / 9.6875 / -0.000742487523747587 / 1.7346039701045204 | [NPY](tensors/0000346.npy) |
| 347 | `model.layers.8.self_attn.o_proj` | 0 | `input.args[0]` | [1, 174, 4096] | torch.bfloat16 → float32 | -7.21875 / 7.0 / 0.00010213401768872205 / 0.866613783550545 | [NPY](tensors/0000347.npy) |
| 348 | `model.layers.8.self_attn.o_proj` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -198.0 / 212.0 / 0.0011246510591039179 / 3.0947631667954782 | [NPY](tensors/0000348.npy) |
| 349 | `model.layers.8.self_attn` | 0 | `output[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -198.0 / 212.0 / 0.0011246510591039179 / 3.0947631667954782 | [NPY](tensors/0000349.npy) |
| 350 | `model.layers.8.self_attn` | 0 | `output[1]` | [1, 64, 174, 174] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0035274876765610326 / 0.025335394425060682 | [NPY](tensors/0000350.npy) |
| 351 | `model.layers.8.post_attention_layernorm` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -41472.0 / 1344.0 / 0.16611172808845687 / 60.00768422626278 | [NPY](tensors/0000351.npy) |
| 352 | `model.layers.8.post_attention_layernorm` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -57.0 / 5.78125 / 0.006779618715179911 / 0.6697450399285166 | [NPY](tensors/0000352.npy) |
| 353 | `model.layers.8.mlp` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -57.0 / 5.78125 / 0.006779618715179911 / 0.6697450399285166 | [NPY](tensors/0000353.npy) |
| 354 | `model.layers.8.mlp.experts` | 0 | `input.args[0]` | [174, 2880] | torch.bfloat16 → float32 | -57.0 / 5.78125 / 0.006779618715179911 / 0.6697450399285166 | [NPY](tensors/0000354.npy) |
| 355 | `model.layers.8.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 356 | `model.layers.8.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 357 | `model.layers.8.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 358 | `model.layers.8.mlp.experts` | 0 | `output` | [174, 2880] | torch.bfloat16 → float32 | -266.0 / 252.0 / 0.06997496207859628 / 5.21479745534413 | [NPY](tensors/0000358.npy) |
| 359 | `model.layers.8.mlp` | 0 | `output[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -266.0 / 252.0 / 0.06997496207859628 / 5.21479745534413 | [NPY](tensors/0000359.npy) |
| 360 | `model.layers.8.mlp` | 0 | `output[1]` | [174, 32] | torch.bfloat16 → float32 | -3.921875 / 3.53125 / -0.1609389110543262 / 0.7549329908299762 | [NPY](tensors/0000360.npy) |
| 361 | `model.layers.8` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -41728.0 / 1136.0 / 0.2358897600898645 / 61.09407140792128 | [NPY](tensors/0000361.npy) |

## Layer 0009

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 362 | `model.layers.9` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -41728.0 / 1136.0 / 0.2358897600898645 / 61.09407140792128 | [NPY](tensors/0000362.npy) |
| 363 | `model.layers.9` | 0 | `input.kwargs['attention_mask']` | [1, 1, 174, 174] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6850256618980335e+38 / 1.6947377057948597e+38 | [NPY](tensors/0000363.npy) |
| 364 | `model.layers.9` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8449686751968559 / 0.8475634832262998 | [NPY](tensors/0000364.npy) |
| 365 | `model.layers.9` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11834632235160365 / 0.6025126921634434 | [NPY](tensors/0000365.npy) |
| 366 | `model.layers.9` | 0 | `input.kwargs['position_ids']` | [1, 174] | torch.int64 → int64 | 0.0 / 173.0 / 86.5 / 50.22864388639879 | [NPY](tensors/0000366.npy) |
| 367 | `model.layers.9` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 368 | `model.layers.9` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 369 | `model.layers.9` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 370 | `model.layers.9.input_layernorm` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -41728.0 / 1136.0 / 0.2358897600898645 / 61.09407140792128 | [NPY](tensors/0000370.npy) |
| 371 | `model.layers.9.input_layernorm` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -207.0 / 72.5 / 0.037662458119825916 / 1.7992845109470421 | [NPY](tensors/0000371.npy) |
| 372 | `model.layers.9.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 174, 2880] | torch.bfloat16 → float32 | -207.0 / 72.5 / 0.037662458119825916 / 1.7992845109470421 | [NPY](tensors/0000372.npy) |
| 373 | `model.layers.9.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 174, 174] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6850256618980335e+38 / 1.6947377057948597e+38 | [NPY](tensors/0000373.npy) |
| 374 | `model.layers.9.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 174] | torch.int64 → int64 | 0.0 / 173.0 / 86.5 / 50.22864388639879 | [NPY](tensors/0000374.npy) |
| 375 | `model.layers.9.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 376 | `model.layers.9.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 377 | `model.layers.9.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8449686751968559 / 0.8475634832262998 | [NPY](tensors/0000377.npy) |
| 378 | `model.layers.9.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11834632235160365 / 0.6025126921634434 | [NPY](tensors/0000378.npy) |
| 379 | `model.layers.9.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 380 | `model.layers.9.self_attn.q_proj` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -207.0 / 72.5 / 0.037662458119825916 / 1.7992845109470421 | [NPY](tensors/0000380.npy) |
| 381 | `model.layers.9.self_attn.q_proj` | 0 | `output` | [1, 174, 4096] | torch.bfloat16 → float32 | -10.1875 / 20.25 / 0.0673591103219098 / 1.2636864601096296 | [NPY](tensors/0000381.npy) |
| 382 | `model.layers.9.self_attn.k_proj` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -207.0 / 72.5 / 0.037662458119825916 / 1.7992845109470421 | [NPY](tensors/0000382.npy) |
| 383 | `model.layers.9.self_attn.k_proj` | 0 | `output` | [1, 174, 512] | torch.bfloat16 → float32 | -50.25 / 40.75 / 0.06782887445698524 / 3.831743086567312 | [NPY](tensors/0000383.npy) |
| 384 | `model.layers.9.self_attn.v_proj` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -207.0 / 72.5 / 0.037662458119825916 / 1.7992845109470421 | [NPY](tensors/0000384.npy) |
| 385 | `model.layers.9.self_attn.v_proj` | 0 | `output` | [1, 174, 512] | torch.bfloat16 → float32 | -27.75 / 12.375 / -0.013878394903122693 / 1.51523508970005 | [NPY](tensors/0000385.npy) |
| 386 | `model.layers.9.self_attn.o_proj` | 0 | `input.args[0]` | [1, 174, 4096] | torch.bfloat16 → float32 | -11.0 / 8.8125 / -0.0044003524983011735 / 0.6478107675377911 | [NPY](tensors/0000386.npy) |
| 387 | `model.layers.9.self_attn.o_proj` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -348.0 / 344.0 / 0.011170850849162077 / 3.913068558144709 | [NPY](tensors/0000387.npy) |
| 388 | `model.layers.9.self_attn` | 0 | `output[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -348.0 / 344.0 / 0.011170850849162077 / 3.913068558144709 | [NPY](tensors/0000388.npy) |
| 389 | `model.layers.9.self_attn` | 0 | `output[1]` | [1, 64, 174, 174] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0042819953738529185 / 0.027263749859948713 | [NPY](tensors/0000389.npy) |
| 390 | `model.layers.9.post_attention_layernorm` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -41728.0 / 1480.0 / 0.24704659667203863 / 60.96372847704353 | [NPY](tensors/0000390.npy) |
| 391 | `model.layers.9.post_attention_layernorm` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -64.5 / 6.375 / 0.007734116737280009 / 0.6887917868785874 | [NPY](tensors/0000391.npy) |
| 392 | `model.layers.9.mlp` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -64.5 / 6.375 / 0.007734116737280009 / 0.6887917868785874 | [NPY](tensors/0000392.npy) |
| 393 | `model.layers.9.mlp.experts` | 0 | `input.args[0]` | [174, 2880] | torch.bfloat16 → float32 | -64.5 / 6.375 / 0.007734116737280009 / 0.6887917868785874 | [NPY](tensors/0000393.npy) |
| 394 | `model.layers.9.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 395 | `model.layers.9.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 396 | `model.layers.9.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 397 | `model.layers.9.mlp.experts` | 0 | `output` | [174, 2880] | torch.bfloat16 → float32 | -568.0 / 636.0 / 0.04822678917669245 / 5.792976432285728 | [NPY](tensors/0000397.npy) |
| 398 | `model.layers.9.mlp` | 0 | `output[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -568.0 / 636.0 / 0.04822678917669245 / 5.792976432285728 | [NPY](tensors/0000398.npy) |
| 399 | `model.layers.9.mlp` | 0 | `output[1]` | [174, 32] | torch.bfloat16 → float32 | -5.1875 / 6.40625 / -0.13031510649056272 / 0.6438073137800417 | [NPY](tensors/0000399.npy) |
| 400 | `model.layers.9` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -41216.0 / 912.0 / 0.29540795731818537 / 61.13691992685412 | [NPY](tensors/0000400.npy) |

## Layer 0010

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 401 | `model.layers.10` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -41216.0 / 912.0 / 0.29540795731818537 / 61.13691992685412 | [NPY](tensors/0000401.npy) |
| 402 | `model.layers.10` | 0 | `input.kwargs['attention_mask']` | [1, 1, 174, 174] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.8060483674001114e+38 / 1.6911081947706832e+38 | [NPY](tensors/0000402.npy) |
| 403 | `model.layers.10` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8449686751968559 / 0.8475634832262998 | [NPY](tensors/0000403.npy) |
| 404 | `model.layers.10` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11834632235160365 / 0.6025126921634434 | [NPY](tensors/0000404.npy) |
| 405 | `model.layers.10` | 0 | `input.kwargs['position_ids']` | [1, 174] | torch.int64 → int64 | 0.0 / 173.0 / 86.5 / 50.22864388639879 | [NPY](tensors/0000405.npy) |
| 406 | `model.layers.10` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 407 | `model.layers.10` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 408 | `model.layers.10` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 409 | `model.layers.10.input_layernorm` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -41216.0 / 912.0 / 0.29540795731818537 / 61.13691992685412 | [NPY](tensors/0000409.npy) |
| 410 | `model.layers.10.input_layernorm` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -109.0 / 49.75 / 0.031205610153747017 / 1.5373942802059677 | [NPY](tensors/0000410.npy) |
| 411 | `model.layers.10.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 174, 2880] | torch.bfloat16 → float32 | -109.0 / 49.75 / 0.031205610153747017 / 1.5373942802059677 | [NPY](tensors/0000411.npy) |
| 412 | `model.layers.10.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 174, 174] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.8060483674001114e+38 / 1.6911081947706832e+38 | [NPY](tensors/0000412.npy) |
| 413 | `model.layers.10.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 174] | torch.int64 → int64 | 0.0 / 173.0 / 86.5 / 50.22864388639879 | [NPY](tensors/0000413.npy) |
| 414 | `model.layers.10.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 415 | `model.layers.10.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 416 | `model.layers.10.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8449686751968559 / 0.8475634832262998 | [NPY](tensors/0000416.npy) |
| 417 | `model.layers.10.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11834632235160365 / 0.6025126921634434 | [NPY](tensors/0000417.npy) |
| 418 | `model.layers.10.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 419 | `model.layers.10.self_attn.q_proj` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -109.0 / 49.75 / 0.031205610153747017 / 1.5373942802059677 | [NPY](tensors/0000419.npy) |
| 420 | `model.layers.10.self_attn.q_proj` | 0 | `output` | [1, 174, 4096] | torch.bfloat16 → float32 | -15.5 / 16.125 / 0.03418517422286296 / 1.098776249510406 | [NPY](tensors/0000420.npy) |
| 421 | `model.layers.10.self_attn.k_proj` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -109.0 / 49.75 / 0.031205610153747017 / 1.5373942802059677 | [NPY](tensors/0000421.npy) |
| 422 | `model.layers.10.self_attn.k_proj` | 0 | `output` | [1, 174, 512] | torch.bfloat16 → float32 | -56.75 / 16.875 / -0.06843370173511834 / 2.431110659182261 | [NPY](tensors/0000422.npy) |
| 423 | `model.layers.10.self_attn.v_proj` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -109.0 / 49.75 / 0.031205610153747017 / 1.5373942802059677 | [NPY](tensors/0000423.npy) |
| 424 | `model.layers.10.self_attn.v_proj` | 0 | `output` | [1, 174, 512] | torch.bfloat16 → float32 | -9.6875 / 10.5625 / 0.06703867540619839 / 2.1411293139495955 | [NPY](tensors/0000424.npy) |
| 425 | `model.layers.10.self_attn.o_proj` | 0 | `input.args[0]` | [1, 174, 4096] | torch.bfloat16 → float32 | -7.46875 / 8.4375 / 0.04431213817696224 / 1.0045522609669038 | [NPY](tensors/0000425.npy) |
| 426 | `model.layers.10.self_attn.o_proj` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -201.0 / 210.0 / 0.03927802949998704 / 4.325527623492865 | [NPY](tensors/0000426.npy) |
| 427 | `model.layers.10.self_attn` | 0 | `output[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -201.0 / 210.0 / 0.03927802949998704 / 4.325527623492865 | [NPY](tensors/0000427.npy) |
| 428 | `model.layers.10.self_attn` | 0 | `output[1]` | [1, 64, 174, 174] | torch.bfloat16 → float32 | 0.0 / 0.984375 / 0.0034470321077821335 / 0.020232845198443553 | [NPY](tensors/0000428.npy) |
| 429 | `model.layers.10.post_attention_layernorm` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -41216.0 / 924.0 / 0.3347359677498368 / 60.94856883007481 | [NPY](tensors/0000429.npy) |
| 430 | `model.layers.10.post_attention_layernorm` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -46.75 / 6.25 / 0.010075855357655697 / 0.7449498671542972 | [NPY](tensors/0000430.npy) |
| 431 | `model.layers.10.mlp` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -46.75 / 6.25 / 0.010075855357655697 / 0.7449498671542972 | [NPY](tensors/0000431.npy) |
| 432 | `model.layers.10.mlp.experts` | 0 | `input.args[0]` | [174, 2880] | torch.bfloat16 → float32 | -46.75 / 6.25 / 0.010075855357655697 / 0.7449498671542972 | [NPY](tensors/0000432.npy) |
| 433 | `model.layers.10.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 434 | `model.layers.10.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 435 | `model.layers.10.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 436 | `model.layers.10.mlp.experts` | 0 | `output` | [174, 2880] | torch.bfloat16 → float32 | -712.0 / 896.0 / 0.14639926499914316 / 8.865067026487518 | [NPY](tensors/0000436.npy) |
| 437 | `model.layers.10.mlp` | 0 | `output[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -712.0 / 896.0 / 0.14639926499914316 / 8.865067026487518 | [NPY](tensors/0000437.npy) |
| 438 | `model.layers.10.mlp` | 0 | `output[1]` | [174, 32] | torch.bfloat16 → float32 | -5.3125 / 4.03125 / -0.12465211166732612 / 0.6785493621737043 | [NPY](tensors/0000438.npy) |
| 439 | `model.layers.10` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -41216.0 / 816.0 / 0.4812072359282395 / 62.67269585697024 | [NPY](tensors/0000439.npy) |

## Layer 0011

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 440 | `model.layers.11` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -41216.0 / 816.0 / 0.4812072359282395 / 62.67269585697024 | [NPY](tensors/0000440.npy) |
| 441 | `model.layers.11` | 0 | `input.kwargs['attention_mask']` | [1, 1, 174, 174] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6850256618980335e+38 / 1.6947377057948597e+38 | [NPY](tensors/0000441.npy) |
| 442 | `model.layers.11` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8449686751968559 / 0.8475634832262998 | [NPY](tensors/0000442.npy) |
| 443 | `model.layers.11` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11834632235160365 / 0.6025126921634434 | [NPY](tensors/0000443.npy) |
| 444 | `model.layers.11` | 0 | `input.kwargs['position_ids']` | [1, 174] | torch.int64 → int64 | 0.0 / 173.0 / 86.5 / 50.22864388639879 | [NPY](tensors/0000444.npy) |
| 445 | `model.layers.11` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 446 | `model.layers.11` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 447 | `model.layers.11` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 448 | `model.layers.11.input_layernorm` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -41216.0 / 816.0 / 0.4812072359282395 / 62.67269585697024 | [NPY](tensors/0000448.npy) |
| 449 | `model.layers.11.input_layernorm` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -191.0 / 135.0 / 0.06464009334619894 / 3.200235539614166 | [NPY](tensors/0000449.npy) |
| 450 | `model.layers.11.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 174, 2880] | torch.bfloat16 → float32 | -191.0 / 135.0 / 0.06464009334619894 / 3.200235539614166 | [NPY](tensors/0000450.npy) |
| 451 | `model.layers.11.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 174, 174] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6850256618980335e+38 / 1.6947377057948597e+38 | [NPY](tensors/0000451.npy) |
| 452 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 174] | torch.int64 → int64 | 0.0 / 173.0 / 86.5 / 50.22864388639879 | [NPY](tensors/0000452.npy) |
| 453 | `model.layers.11.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 454 | `model.layers.11.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 455 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8449686751968559 / 0.8475634832262998 | [NPY](tensors/0000455.npy) |
| 456 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11834632235160365 / 0.6025126921634434 | [NPY](tensors/0000456.npy) |
| 457 | `model.layers.11.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 458 | `model.layers.11.self_attn.q_proj` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -191.0 / 135.0 / 0.06464009334619894 / 3.200235539614166 | [NPY](tensors/0000458.npy) |
| 459 | `model.layers.11.self_attn.q_proj` | 0 | `output` | [1, 174, 4096] | torch.bfloat16 → float32 | -11.25 / 13.3125 / 0.03541164366762895 / 1.329811815127657 | [NPY](tensors/0000459.npy) |
| 460 | `model.layers.11.self_attn.k_proj` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -191.0 / 135.0 / 0.06464009334619894 / 3.200235539614166 | [NPY](tensors/0000460.npy) |
| 461 | `model.layers.11.self_attn.k_proj` | 0 | `output` | [1, 174, 512] | torch.bfloat16 → float32 | -38.25 / 45.25 / 0.053554490224683074 / 3.5971363675557715 | [NPY](tensors/0000461.npy) |
| 462 | `model.layers.11.self_attn.v_proj` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -191.0 / 135.0 / 0.06464009334619894 / 3.200235539614166 | [NPY](tensors/0000462.npy) |
| 463 | `model.layers.11.self_attn.v_proj` | 0 | `output` | [1, 174, 512] | torch.bfloat16 → float32 | -15.9375 / 22.125 / -0.038327308221795094 / 2.4750020746389514 | [NPY](tensors/0000463.npy) |
| 464 | `model.layers.11.self_attn.o_proj` | 0 | `input.args[0]` | [1, 174, 4096] | torch.bfloat16 → float32 | -11.75 / 11.25 / -0.029415455013632113 / 1.41494034335517 | [NPY](tensors/0000464.npy) |
| 465 | `model.layers.11.self_attn.o_proj` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -466.0 / 500.0 / -0.059633685190511314 / 7.347280343395959 | [NPY](tensors/0000465.npy) |
| 466 | `model.layers.11.self_attn` | 0 | `output[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -466.0 / 500.0 / -0.059633685190511314 / 7.347280343395959 | [NPY](tensors/0000466.npy) |
| 467 | `model.layers.11.self_attn` | 0 | `output[1]` | [1, 64, 174, 174] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.004626363628457285 / 0.024433900765461487 | [NPY](tensors/0000467.npy) |
| 468 | `model.layers.11.post_attention_layernorm` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -41216.0 / 692.0 / 0.42153273457007084 / 61.78235652692705 | [NPY](tensors/0000468.npy) |
| 469 | `model.layers.11.post_attention_layernorm` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -78.5 / 7.3125 / 0.008975856068471533 / 0.8002378851118439 | [NPY](tensors/0000469.npy) |
| 470 | `model.layers.11.mlp` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -78.5 / 7.3125 / 0.008975856068471533 / 0.8002378851118439 | [NPY](tensors/0000470.npy) |
| 471 | `model.layers.11.mlp.experts` | 0 | `input.args[0]` | [174, 2880] | torch.bfloat16 → float32 | -78.5 / 7.3125 / 0.008975856068471533 / 0.8002378851118439 | [NPY](tensors/0000471.npy) |
| 472 | `model.layers.11.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 473 | `model.layers.11.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 474 | `model.layers.11.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 475 | `model.layers.11.mlp.experts` | 0 | `output` | [174, 2880] | torch.bfloat16 → float32 | -490.0 / 386.0 / 0.12563853368905312 / 9.855218355617675 | [NPY](tensors/0000475.npy) |
| 476 | `model.layers.11.mlp` | 0 | `output[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -490.0 / 386.0 / 0.12563853368905312 / 9.855218355617675 | [NPY](tensors/0000476.npy) |
| 477 | `model.layers.11.mlp` | 0 | `output[1]` | [174, 32] | torch.bfloat16 → float32 | -10.75 / 2.875 / -0.16575130374952293 / 0.818547923805975 | [NPY](tensors/0000477.npy) |
| 478 | `model.layers.11` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -41216.0 / 832.0 / 0.5471793436608248 / 63.94375157375799 | [NPY](tensors/0000478.npy) |

## Layer 0012

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 479 | `model.layers.12` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -41216.0 / 832.0 / 0.5471793436608248 / 63.94375157375799 | [NPY](tensors/0000479.npy) |
| 480 | `model.layers.12` | 0 | `input.kwargs['attention_mask']` | [1, 1, 174, 174] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.8060483674001114e+38 / 1.6911081947706832e+38 | [NPY](tensors/0000480.npy) |
| 481 | `model.layers.12` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8449686751968559 / 0.8475634832262998 | [NPY](tensors/0000481.npy) |
| 482 | `model.layers.12` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11834632235160365 / 0.6025126921634434 | [NPY](tensors/0000482.npy) |
| 483 | `model.layers.12` | 0 | `input.kwargs['position_ids']` | [1, 174] | torch.int64 → int64 | 0.0 / 173.0 / 86.5 / 50.22864388639879 | [NPY](tensors/0000483.npy) |
| 484 | `model.layers.12` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 485 | `model.layers.12` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 486 | `model.layers.12` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 487 | `model.layers.12.input_layernorm` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -41216.0 / 832.0 / 0.5471793436608248 / 63.94375157375799 | [NPY](tensors/0000487.npy) |
| 488 | `model.layers.12.input_layernorm` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -136.0 / 44.25 / 0.03880374128222561 / 1.5957280442642976 | [NPY](tensors/0000488.npy) |
| 489 | `model.layers.12.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 174, 2880] | torch.bfloat16 → float32 | -136.0 / 44.25 / 0.03880374128222561 / 1.5957280442642976 | [NPY](tensors/0000489.npy) |
| 490 | `model.layers.12.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 174, 174] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.8060483674001114e+38 / 1.6911081947706832e+38 | [NPY](tensors/0000490.npy) |
| 491 | `model.layers.12.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 174] | torch.int64 → int64 | 0.0 / 173.0 / 86.5 / 50.22864388639879 | [NPY](tensors/0000491.npy) |
| 492 | `model.layers.12.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 493 | `model.layers.12.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 494 | `model.layers.12.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8449686751968559 / 0.8475634832262998 | [NPY](tensors/0000494.npy) |
| 495 | `model.layers.12.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11834632235160365 / 0.6025126921634434 | [NPY](tensors/0000495.npy) |
| 496 | `model.layers.12.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 497 | `model.layers.12.self_attn.q_proj` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -136.0 / 44.25 / 0.03880374128222561 / 1.5957280442642976 | [NPY](tensors/0000497.npy) |
| 498 | `model.layers.12.self_attn.q_proj` | 0 | `output` | [1, 174, 4096] | torch.bfloat16 → float32 | -19.75 / 18.125 / -0.016087537623322018 / 1.363080859045006 | [NPY](tensors/0000498.npy) |
| 499 | `model.layers.12.self_attn.k_proj` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -136.0 / 44.25 / 0.03880374128222561 / 1.5957280442642976 | [NPY](tensors/0000499.npy) |
| 500 | `model.layers.12.self_attn.k_proj` | 0 | `output` | [1, 174, 512] | torch.bfloat16 → float32 | -12.8125 / 13.0625 / 0.0002961172454658597 / 1.3339334199304285 | [NPY](tensors/0000500.npy) |
| 501 | `model.layers.12.self_attn.v_proj` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -136.0 / 44.25 / 0.03880374128222561 / 1.5957280442642976 | [NPY](tensors/0000501.npy) |
| 502 | `model.layers.12.self_attn.v_proj` | 0 | `output` | [1, 174, 512] | torch.bfloat16 → float32 | -17.125 / 19.5 / -0.0012005352597127018 / 2.8336589942458685 | [NPY](tensors/0000502.npy) |
| 503 | `model.layers.12.self_attn.o_proj` | 0 | `input.args[0]` | [1, 174, 4096] | torch.bfloat16 → float32 | -10.625 / 10.6875 / -0.015827975816029478 / 1.4503095076705452 | [NPY](tensors/0000503.npy) |
| 504 | `model.layers.12.self_attn.o_proj` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -288.0 / 324.0 / -0.045578991094340084 / 6.071823611664549 | [NPY](tensors/0000504.npy) |
| 505 | `model.layers.12.self_attn` | 0 | `output[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -288.0 / 324.0 / -0.045578991094340084 / 6.071823611664549 | [NPY](tensors/0000505.npy) |
| 506 | `model.layers.12.self_attn` | 0 | `output[1]` | [1, 64, 174, 174] | torch.bfloat16 → float32 | 0.0 / 0.96875 / 0.0036088758865900445 / 0.020843571834169097 | [NPY](tensors/0000506.npy) |
| 507 | `model.layers.12.post_attention_layernorm` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -41216.0 / 700.0 / 0.5016734382658626 / 63.31456242924387 | [NPY](tensors/0000507.npy) |
| 508 | `model.layers.12.post_attention_layernorm` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -83.5 / 6.59375 / 0.008625386218572484 / 0.845066011340614 | [NPY](tensors/0000508.npy) |
| 509 | `model.layers.12.mlp` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -83.5 / 6.59375 / 0.008625386218572484 / 0.845066011340614 | [NPY](tensors/0000509.npy) |
| 510 | `model.layers.12.mlp.experts` | 0 | `input.args[0]` | [174, 2880] | torch.bfloat16 → float32 | -83.5 / 6.59375 / 0.008625386218572484 / 0.845066011340614 | [NPY](tensors/0000510.npy) |
| 511 | `model.layers.12.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 512 | `model.layers.12.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 513 | `model.layers.12.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 514 | `model.layers.12.mlp.experts` | 0 | `output` | [174, 2880] | torch.bfloat16 → float32 | -1688.0 / 1496.0 / 0.16496371961606718 / 13.325419138316564 | [NPY](tensors/0000514.npy) |
| 515 | `model.layers.12.mlp` | 0 | `output[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -1688.0 / 1496.0 / 0.16496371961606718 / 13.325419138316564 | [NPY](tensors/0000515.npy) |
| 516 | `model.layers.12.mlp` | 0 | `output[1]` | [174, 32] | torch.bfloat16 → float32 | -6.9375 / 3.8125 / -0.15758102241603808 / 0.8260493217124939 | [NPY](tensors/0000516.npy) |
| 517 | `model.layers.12` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -41216.0 / 1808.0 / 0.666717073287087 / 66.9646271002261 | [NPY](tensors/0000517.npy) |

## Layer 0013

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 518 | `model.layers.13` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -41216.0 / 1808.0 / 0.666717073287087 / 66.9646271002261 | [NPY](tensors/0000518.npy) |
| 519 | `model.layers.13` | 0 | `input.kwargs['attention_mask']` | [1, 1, 174, 174] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6850256618980335e+38 / 1.6947377057948597e+38 | [NPY](tensors/0000519.npy) |
| 520 | `model.layers.13` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8449686751968559 / 0.8475634832262998 | [NPY](tensors/0000520.npy) |
| 521 | `model.layers.13` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11834632235160365 / 0.6025126921634434 | [NPY](tensors/0000521.npy) |
| 522 | `model.layers.13` | 0 | `input.kwargs['position_ids']` | [1, 174] | torch.int64 → int64 | 0.0 / 173.0 / 86.5 / 50.22864388639879 | [NPY](tensors/0000522.npy) |
| 523 | `model.layers.13` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 524 | `model.layers.13` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 525 | `model.layers.13` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 526 | `model.layers.13.input_layernorm` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -41216.0 / 1808.0 / 0.666717073287087 / 66.9646271002261 | [NPY](tensors/0000526.npy) |
| 527 | `model.layers.13.input_layernorm` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -182.0 / 99.0 / 0.06031703577599326 / 2.9068886585521923 | [NPY](tensors/0000527.npy) |
| 528 | `model.layers.13.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 174, 2880] | torch.bfloat16 → float32 | -182.0 / 99.0 / 0.06031703577599326 / 2.9068886585521923 | [NPY](tensors/0000528.npy) |
| 529 | `model.layers.13.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 174, 174] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6850256618980335e+38 / 1.6947377057948597e+38 | [NPY](tensors/0000529.npy) |
| 530 | `model.layers.13.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 174] | torch.int64 → int64 | 0.0 / 173.0 / 86.5 / 50.22864388639879 | [NPY](tensors/0000530.npy) |
| 531 | `model.layers.13.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 532 | `model.layers.13.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 533 | `model.layers.13.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8449686751968559 / 0.8475634832262998 | [NPY](tensors/0000533.npy) |
| 534 | `model.layers.13.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11834632235160365 / 0.6025126921634434 | [NPY](tensors/0000534.npy) |
| 535 | `model.layers.13.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 536 | `model.layers.13.self_attn.q_proj` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -182.0 / 99.0 / 0.06031703577599326 / 2.9068886585521923 | [NPY](tensors/0000536.npy) |
| 537 | `model.layers.13.self_attn.q_proj` | 0 | `output` | [1, 174, 4096] | torch.bfloat16 → float32 | -10.75 / 12.6875 / 0.04002648272405074 / 1.3984200106542 | [NPY](tensors/0000537.npy) |
| 538 | `model.layers.13.self_attn.k_proj` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -182.0 / 99.0 / 0.06031703577599326 / 2.9068886585521923 | [NPY](tensors/0000538.npy) |
| 539 | `model.layers.13.self_attn.k_proj` | 0 | `output` | [1, 174, 512] | torch.bfloat16 → float32 | -54.0 / 31.25 / -0.32528090846307317 / 3.9841766808007595 | [NPY](tensors/0000539.npy) |
| 540 | `model.layers.13.self_attn.v_proj` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -182.0 / 99.0 / 0.06031703577599326 / 2.9068886585521923 | [NPY](tensors/0000540.npy) |
| 541 | `model.layers.13.self_attn.v_proj` | 0 | `output` | [1, 174, 512] | torch.bfloat16 → float32 | -16.5 / 22.5 / 0.007723029831360126 / 2.8167491247445886 | [NPY](tensors/0000541.npy) |
| 542 | `model.layers.13.self_attn.o_proj` | 0 | `input.args[0]` | [1, 174, 4096] | torch.bfloat16 → float32 | -11.125 / 20.875 / -0.002450954048329428 / 1.6041444710734758 | [NPY](tensors/0000542.npy) |
| 543 | `model.layers.13.self_attn.o_proj` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -564.0 / 1184.0 / -0.09279558917476009 / 9.669330208542254 | [NPY](tensors/0000543.npy) |
| 544 | `model.layers.13.self_attn` | 0 | `output[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -564.0 / 1184.0 / -0.09279558917476009 / 9.669330208542254 | [NPY](tensors/0000544.npy) |
| 545 | `model.layers.13.self_attn` | 0 | `output[1]` | [1, 64, 174, 174] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.005063793701775368 / 0.024796423785700034 | [NPY](tensors/0000545.npy) |
| 546 | `model.layers.13.post_attention_layernorm` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -41216.0 / 1280.0 / 0.5739741387495136 / 65.37474142103859 | [NPY](tensors/0000546.npy) |
| 547 | `model.layers.13.post_attention_layernorm` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -86.0 / 6.4375 / 0.006621300032133971 / 0.9236205306364459 | [NPY](tensors/0000547.npy) |
| 548 | `model.layers.13.mlp` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -86.0 / 6.4375 / 0.006621300032133971 / 0.9236205306364459 | [NPY](tensors/0000548.npy) |
| 549 | `model.layers.13.mlp.experts` | 0 | `input.args[0]` | [174, 2880] | torch.bfloat16 → float32 | -86.0 / 6.4375 / 0.006621300032133971 / 0.9236205306364459 | [NPY](tensors/0000549.npy) |
| 550 | `model.layers.13.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 551 | `model.layers.13.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 552 | `model.layers.13.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 553 | `model.layers.13.mlp.experts` | 0 | `output` | [174, 2880] | torch.bfloat16 → float32 | -476.0 / 560.0 / 0.07753688043713722 / 13.328648233107128 | [NPY](tensors/0000553.npy) |
| 554 | `model.layers.13.mlp` | 0 | `output[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -476.0 / 560.0 / 0.07753688043713722 / 13.328648233107128 | [NPY](tensors/0000554.npy) |
| 555 | `model.layers.13.mlp` | 0 | `output[1]` | [174, 32] | torch.bfloat16 → float32 | -5.46875 / 3.796875 / -0.18142872774738006 / 0.8699297820731704 | [NPY](tensors/0000555.npy) |
| 556 | `model.layers.13` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -41216.0 / 1144.0 / 0.6514036127433923 / 69.27658874813231 | [NPY](tensors/0000556.npy) |

## Layer 0014

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 557 | `model.layers.14` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -41216.0 / 1144.0 / 0.6514036127433923 / 69.27658874813231 | [NPY](tensors/0000557.npy) |
| 558 | `model.layers.14` | 0 | `input.kwargs['attention_mask']` | [1, 1, 174, 174] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.8060483674001114e+38 / 1.6911081947706832e+38 | [NPY](tensors/0000558.npy) |
| 559 | `model.layers.14` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8449686751968559 / 0.8475634832262998 | [NPY](tensors/0000559.npy) |
| 560 | `model.layers.14` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11834632235160365 / 0.6025126921634434 | [NPY](tensors/0000560.npy) |
| 561 | `model.layers.14` | 0 | `input.kwargs['position_ids']` | [1, 174] | torch.int64 → int64 | 0.0 / 173.0 / 86.5 / 50.22864388639879 | [NPY](tensors/0000561.npy) |
| 562 | `model.layers.14` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 563 | `model.layers.14` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 564 | `model.layers.14` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 565 | `model.layers.14.input_layernorm` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -41216.0 / 1144.0 / 0.6514036127433923 / 69.27658874813231 | [NPY](tensors/0000565.npy) |
| 566 | `model.layers.14.input_layernorm` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -148.0 / 48.5 / 0.04447482502894383 / 1.9516584421557648 | [NPY](tensors/0000566.npy) |
| 567 | `model.layers.14.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 174, 2880] | torch.bfloat16 → float32 | -148.0 / 48.5 / 0.04447482502894383 / 1.9516584421557648 | [NPY](tensors/0000567.npy) |
| 568 | `model.layers.14.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 174, 174] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.8060483674001114e+38 / 1.6911081947706832e+38 | [NPY](tensors/0000568.npy) |
| 569 | `model.layers.14.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 174] | torch.int64 → int64 | 0.0 / 173.0 / 86.5 / 50.22864388639879 | [NPY](tensors/0000569.npy) |
| 570 | `model.layers.14.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 571 | `model.layers.14.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 572 | `model.layers.14.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8449686751968559 / 0.8475634832262998 | [NPY](tensors/0000572.npy) |
| 573 | `model.layers.14.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11834632235160365 / 0.6025126921634434 | [NPY](tensors/0000573.npy) |
| 574 | `model.layers.14.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 575 | `model.layers.14.self_attn.q_proj` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -148.0 / 48.5 / 0.04447482502894383 / 1.9516584421557648 | [NPY](tensors/0000575.npy) |
| 576 | `model.layers.14.self_attn.q_proj` | 0 | `output` | [1, 174, 4096] | torch.bfloat16 → float32 | -53.25 / 29.125 / -0.06283969139346075 / 2.1284789901043593 | [NPY](tensors/0000576.npy) |
| 577 | `model.layers.14.self_attn.k_proj` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -148.0 / 48.5 / 0.04447482502894383 / 1.9516584421557648 | [NPY](tensors/0000577.npy) |
| 578 | `model.layers.14.self_attn.k_proj` | 0 | `output` | [1, 174, 512] | torch.bfloat16 → float32 | -37.75 / 18.875 / 0.04305128196532699 / 1.6382138087061533 | [NPY](tensors/0000578.npy) |
| 579 | `model.layers.14.self_attn.v_proj` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -148.0 / 48.5 / 0.04447482502894383 / 1.9516584421557648 | [NPY](tensors/0000579.npy) |
| 580 | `model.layers.14.self_attn.v_proj` | 0 | `output` | [1, 174, 512] | torch.bfloat16 → float32 | -22.5 / 21.5 / -0.0336695099784725 / 4.700192439229069 | [NPY](tensors/0000580.npy) |
| 581 | `model.layers.14.self_attn.o_proj` | 0 | `input.args[0]` | [1, 174, 4096] | torch.bfloat16 → float32 | -20.375 / 18.0 / -0.029957336634049463 / 2.576882660602521 | [NPY](tensors/0000581.npy) |
| 582 | `model.layers.14.self_attn.o_proj` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -302.0 / 330.0 / -0.04600606145263479 / 8.935888878536483 | [NPY](tensors/0000582.npy) |
| 583 | `model.layers.14.self_attn` | 0 | `output[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -302.0 / 330.0 / -0.04600606145263479 / 8.935888878536483 | [NPY](tensors/0000583.npy) |
| 584 | `model.layers.14.self_attn` | 0 | `output[1]` | [1, 64, 174, 174] | torch.bfloat16 → float32 | 0.0 / 0.95703125 / 0.003575089493437711 / 0.02465833769657146 | [NPY](tensors/0000584.npy) |
| 585 | `model.layers.14.post_attention_layernorm` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -41216.0 / 924.0 / 0.6052735747048681 / 68.29271303045212 | [NPY](tensors/0000585.npy) |
| 586 | `model.layers.14.post_attention_layernorm` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -99.0 / 8.9375 / 0.007383863660025186 / 1.0040744359742713 | [NPY](tensors/0000586.npy) |
| 587 | `model.layers.14.mlp` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -99.0 / 8.9375 / 0.007383863660025186 / 1.0040744359742713 | [NPY](tensors/0000587.npy) |
| 588 | `model.layers.14.mlp.experts` | 0 | `input.args[0]` | [174, 2880] | torch.bfloat16 → float32 | -99.0 / 8.9375 / 0.007383863660025186 / 1.0040744359742713 | [NPY](tensors/0000588.npy) |
| 589 | `model.layers.14.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 590 | `model.layers.14.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 591 | `model.layers.14.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 592 | `model.layers.14.mlp.experts` | 0 | `output` | [174, 2880] | torch.bfloat16 → float32 | -1280.0 / 1136.0 / 0.04432108310904082 / 19.267580281446165 | [NPY](tensors/0000592.npy) |
| 593 | `model.layers.14.mlp` | 0 | `output[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -1280.0 / 1136.0 / 0.04432108310904082 / 19.267580281446165 | [NPY](tensors/0000593.npy) |
| 594 | `model.layers.14.mlp` | 0 | `output[1]` | [174, 32] | torch.bfloat16 → float32 | -6.84375 / 6.53125 / -0.25219536238703233 / 0.8069510770862778 | [NPY](tensors/0000594.npy) |
| 595 | `model.layers.14` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -41216.0 / 2016.0 / 0.6497023118410074 / 75.52408045701073 | [NPY](tensors/0000595.npy) |

## Layer 0015

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 596 | `model.layers.15` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -41216.0 / 2016.0 / 0.6497023118410074 / 75.52408045701073 | [NPY](tensors/0000596.npy) |
| 597 | `model.layers.15` | 0 | `input.kwargs['attention_mask']` | [1, 1, 174, 174] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6850256618980335e+38 / 1.6947377057948597e+38 | [NPY](tensors/0000597.npy) |
| 598 | `model.layers.15` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8449686751968559 / 0.8475634832262998 | [NPY](tensors/0000598.npy) |
| 599 | `model.layers.15` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11834632235160365 / 0.6025126921634434 | [NPY](tensors/0000599.npy) |
| 600 | `model.layers.15` | 0 | `input.kwargs['position_ids']` | [1, 174] | torch.int64 → int64 | 0.0 / 173.0 / 86.5 / 50.22864388639879 | [NPY](tensors/0000600.npy) |
| 601 | `model.layers.15` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 602 | `model.layers.15` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 603 | `model.layers.15` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 604 | `model.layers.15.input_layernorm` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -41216.0 / 2016.0 / 0.6497023118410074 / 75.52408045701073 | [NPY](tensors/0000604.npy) |
| 605 | `model.layers.15.input_layernorm` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -164.0 / 65.0 / 0.045009400716496305 / 2.1949007381438 | [NPY](tensors/0000605.npy) |
| 606 | `model.layers.15.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 174, 2880] | torch.bfloat16 → float32 | -164.0 / 65.0 / 0.045009400716496305 / 2.1949007381438 | [NPY](tensors/0000606.npy) |
| 607 | `model.layers.15.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 174, 174] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6850256618980335e+38 / 1.6947377057948597e+38 | [NPY](tensors/0000607.npy) |
| 608 | `model.layers.15.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 174] | torch.int64 → int64 | 0.0 / 173.0 / 86.5 / 50.22864388639879 | [NPY](tensors/0000608.npy) |
| 609 | `model.layers.15.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 610 | `model.layers.15.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 611 | `model.layers.15.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8449686751968559 / 0.8475634832262998 | [NPY](tensors/0000611.npy) |
| 612 | `model.layers.15.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11834632235160365 / 0.6025126921634434 | [NPY](tensors/0000612.npy) |
| 613 | `model.layers.15.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 614 | `model.layers.15.self_attn.q_proj` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -164.0 / 65.0 / 0.045009400716496305 / 2.1949007381438 | [NPY](tensors/0000614.npy) |
| 615 | `model.layers.15.self_attn.q_proj` | 0 | `output` | [1, 174, 4096] | torch.bfloat16 → float32 | -21.25 / 16.375 / 0.00819012571412912 / 1.4454422379206684 | [NPY](tensors/0000615.npy) |
| 616 | `model.layers.15.self_attn.k_proj` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -164.0 / 65.0 / 0.045009400716496305 / 2.1949007381438 | [NPY](tensors/0000616.npy) |
| 617 | `model.layers.15.self_attn.k_proj` | 0 | `output` | [1, 174, 512] | torch.bfloat16 → float32 | -36.75 / 51.25 / 0.03235707020965116 / 4.0568152432769375 | [NPY](tensors/0000617.npy) |
| 618 | `model.layers.15.self_attn.v_proj` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -164.0 / 65.0 / 0.045009400716496305 / 2.1949007381438 | [NPY](tensors/0000618.npy) |
| 619 | `model.layers.15.self_attn.v_proj` | 0 | `output` | [1, 174, 512] | torch.bfloat16 → float32 | -61.5 / 38.5 / -0.13525172939588284 / 2.8414453994768496 | [NPY](tensors/0000619.npy) |
| 620 | `model.layers.15.self_attn.o_proj` | 0 | `input.args[0]` | [1, 174, 4096] | torch.bfloat16 → float32 | -11.75 / 20.375 / -0.09062405380877682 / 1.3799664624387271 | [NPY](tensors/0000620.npy) |
| 621 | `model.layers.15.self_attn.o_proj` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -1680.0 / 1704.0 / -0.02551649556772386 / 13.312400567931922 | [NPY](tensors/0000621.npy) |
| 622 | `model.layers.15.self_attn` | 0 | `output[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -1680.0 / 1704.0 / -0.02551649556772386 / 13.312400567931922 | [NPY](tensors/0000622.npy) |
| 623 | `model.layers.15.self_attn` | 0 | `output[1]` | [1, 64, 174, 174] | torch.bfloat16 → float32 | 0.0 / 0.9921875 / 0.0039831602664563365 / 0.022095185016310265 | [NPY](tensors/0000623.npy) |
| 624 | `model.layers.15.post_attention_layernorm` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -41216.0 / 1136.0 / 0.6241846357421096 / 73.44317807305136 | [NPY](tensors/0000624.npy) |
| 625 | `model.layers.15.post_attention_layernorm` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -106.0 / 9.375 / 0.008709428626877444 / 1.0091737473093254 | [NPY](tensors/0000625.npy) |
| 626 | `model.layers.15.mlp` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -106.0 / 9.375 / 0.008709428626877444 / 1.0091737473093254 | [NPY](tensors/0000626.npy) |
| 627 | `model.layers.15.mlp.experts` | 0 | `input.args[0]` | [174, 2880] | torch.bfloat16 → float32 | -106.0 / 9.375 / 0.008709428626877444 / 1.0091737473093254 | [NPY](tensors/0000627.npy) |
| 628 | `model.layers.15.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 629 | `model.layers.15.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 630 | `model.layers.15.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 631 | `model.layers.15.mlp.experts` | 0 | `output` | [174, 2880] | torch.bfloat16 → float32 | -732.0 / 640.0 / -0.20751365743682149 / 20.884755442696623 | [NPY](tensors/0000631.npy) |
| 632 | `model.layers.15.mlp` | 0 | `output[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -732.0 / 640.0 / -0.20751365743682149 / 20.884755442696623 | [NPY](tensors/0000632.npy) |
| 633 | `model.layers.15.mlp` | 0 | `output[1]` | [174, 32] | torch.bfloat16 → float32 | -5.625 / 4.40625 / -0.2730460016206763 / 0.9571621148660191 | [NPY](tensors/0000633.npy) |
| 634 | `model.layers.15` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -41216.0 / 1432.0 / 0.4164037453564952 / 81.76165821313609 | [NPY](tensors/0000634.npy) |

## Layer 0016

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 635 | `model.layers.16` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -41216.0 / 1432.0 / 0.4164037453564952 / 81.76165821313609 | [NPY](tensors/0000635.npy) |
| 636 | `model.layers.16` | 0 | `input.kwargs['attention_mask']` | [1, 1, 174, 174] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.8060483674001114e+38 / 1.6911081947706832e+38 | [NPY](tensors/0000636.npy) |
| 637 | `model.layers.16` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8449686751968559 / 0.8475634832262998 | [NPY](tensors/0000637.npy) |
| 638 | `model.layers.16` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11834632235160365 / 0.6025126921634434 | [NPY](tensors/0000638.npy) |
| 639 | `model.layers.16` | 0 | `input.kwargs['position_ids']` | [1, 174] | torch.int64 → int64 | 0.0 / 173.0 / 86.5 / 50.22864388639879 | [NPY](tensors/0000639.npy) |
| 640 | `model.layers.16` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 641 | `model.layers.16` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 642 | `model.layers.16` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 643 | `model.layers.16.input_layernorm` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -41216.0 / 1432.0 / 0.4164037453564952 / 81.76165821313609 | [NPY](tensors/0000643.npy) |
| 644 | `model.layers.16.input_layernorm` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -131.0 / 51.25 / 0.030914929257955588 / 1.9123902544982025 | [NPY](tensors/0000644.npy) |
| 645 | `model.layers.16.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 174, 2880] | torch.bfloat16 → float32 | -131.0 / 51.25 / 0.030914929257955588 / 1.9123902544982025 | [NPY](tensors/0000645.npy) |
| 646 | `model.layers.16.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 174, 174] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.8060483674001114e+38 / 1.6911081947706832e+38 | [NPY](tensors/0000646.npy) |
| 647 | `model.layers.16.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 174] | torch.int64 → int64 | 0.0 / 173.0 / 86.5 / 50.22864388639879 | [NPY](tensors/0000647.npy) |
| 648 | `model.layers.16.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 649 | `model.layers.16.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 650 | `model.layers.16.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8449686751968559 / 0.8475634832262998 | [NPY](tensors/0000650.npy) |
| 651 | `model.layers.16.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11834632235160365 / 0.6025126921634434 | [NPY](tensors/0000651.npy) |
| 652 | `model.layers.16.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 653 | `model.layers.16.self_attn.q_proj` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -131.0 / 51.25 / 0.030914929257955588 / 1.9123902544982025 | [NPY](tensors/0000653.npy) |
| 654 | `model.layers.16.self_attn.q_proj` | 0 | `output` | [1, 174, 4096] | torch.bfloat16 → float32 | -25.375 / 27.75 / 0.027746701660048688 / 1.7037923658628775 | [NPY](tensors/0000654.npy) |
| 655 | `model.layers.16.self_attn.k_proj` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -131.0 / 51.25 / 0.030914929257955588 / 1.9123902544982025 | [NPY](tensors/0000655.npy) |
| 656 | `model.layers.16.self_attn.k_proj` | 0 | `output` | [1, 174, 512] | torch.bfloat16 → float32 | -14.9375 / 32.0 / 0.04202736644395467 / 1.6403772976919382 | [NPY](tensors/0000656.npy) |
| 657 | `model.layers.16.self_attn.v_proj` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -131.0 / 51.25 / 0.030914929257955588 / 1.9123902544982025 | [NPY](tensors/0000657.npy) |
| 658 | `model.layers.16.self_attn.v_proj` | 0 | `output` | [1, 174, 512] | torch.bfloat16 → float32 | -22.875 / 19.625 / 0.03860746204167947 / 4.324100062336087 | [NPY](tensors/0000658.npy) |
| 659 | `model.layers.16.self_attn.o_proj` | 0 | `input.args[0]` | [1, 174, 4096] | torch.bfloat16 → float32 | -21.0 / 17.75 / 0.00735884356352791 / 1.9036326688556175 | [NPY](tensors/0000659.npy) |
| 660 | `model.layers.16.self_attn.o_proj` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -552.0 / 552.0 / 0.024322489253929214 / 12.85369182138078 | [NPY](tensors/0000660.npy) |
| 661 | `model.layers.16.self_attn` | 0 | `output[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -552.0 / 552.0 / 0.024322489253929214 / 12.85369182138078 | [NPY](tensors/0000661.npy) |
| 662 | `model.layers.16.self_attn` | 0 | `output[1]` | [1, 64, 174, 174] | torch.bfloat16 → float32 | 0.0 / 0.94140625 / 0.002896383889459857 / 0.020388861125795067 | [NPY](tensors/0000662.npy) |
| 663 | `model.layers.16.post_attention_layernorm` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -41216.0 / 1328.0 / 0.4407574632919915 / 80.89924890835215 | [NPY](tensors/0000663.npy) |
| 664 | `model.layers.16.post_attention_layernorm` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -68.0 / 10.0 / 0.00825725428005954 / 0.9792612885938612 | [NPY](tensors/0000664.npy) |
| 665 | `model.layers.16.mlp` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -68.0 / 10.0 / 0.00825725428005954 / 0.9792612885938612 | [NPY](tensors/0000665.npy) |
| 666 | `model.layers.16.mlp.experts` | 0 | `input.args[0]` | [174, 2880] | torch.bfloat16 → float32 | -68.0 / 10.0 / 0.00825725428005954 / 0.9792612885938612 | [NPY](tensors/0000666.npy) |
| 667 | `model.layers.16.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 668 | `model.layers.16.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 669 | `model.layers.16.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 670 | `model.layers.16.mlp.experts` | 0 | `output` | [174, 2880] | torch.bfloat16 → float32 | -2368.0 / 1728.0 / -0.18010569235374188 / 34.14519739310513 | [NPY](tensors/0000670.npy) |
| 671 | `model.layers.16.mlp` | 0 | `output[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -2368.0 / 1728.0 / -0.18010569235374188 / 34.14519739310513 | [NPY](tensors/0000671.npy) |
| 672 | `model.layers.16.mlp` | 0 | `output[1]` | [174, 32] | torch.bfloat16 → float32 | -6.34375 / 4.46875 / -0.31457938476540576 / 1.25576259723766 | [NPY](tensors/0000672.npy) |
| 673 | `model.layers.16` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -41216.0 / 2656.0 / 0.26083802263398737 / 99.21038367367791 | [NPY](tensors/0000673.npy) |

## Layer 0017

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 674 | `model.layers.17` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -41216.0 / 2656.0 / 0.26083802263398737 / 99.21038367367791 | [NPY](tensors/0000674.npy) |
| 675 | `model.layers.17` | 0 | `input.kwargs['attention_mask']` | [1, 1, 174, 174] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6850256618980335e+38 / 1.6947377057948597e+38 | [NPY](tensors/0000675.npy) |
| 676 | `model.layers.17` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8449686751968559 / 0.8475634832262998 | [NPY](tensors/0000676.npy) |
| 677 | `model.layers.17` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11834632235160365 / 0.6025126921634434 | [NPY](tensors/0000677.npy) |
| 678 | `model.layers.17` | 0 | `input.kwargs['position_ids']` | [1, 174] | torch.int64 → int64 | 0.0 / 173.0 / 86.5 / 50.22864388639879 | [NPY](tensors/0000678.npy) |
| 679 | `model.layers.17` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 680 | `model.layers.17` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 681 | `model.layers.17` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 682 | `model.layers.17.input_layernorm` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -41216.0 / 2656.0 / 0.26083802263398737 / 99.21038367367791 | [NPY](tensors/0000682.npy) |
| 683 | `model.layers.17.input_layernorm` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -124.5 / 87.0 / 0.04068461955354893 / 2.7416266632044977 | [NPY](tensors/0000683.npy) |
| 684 | `model.layers.17.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 174, 2880] | torch.bfloat16 → float32 | -124.5 / 87.0 / 0.04068461955354893 / 2.7416266632044977 | [NPY](tensors/0000684.npy) |
| 685 | `model.layers.17.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 174, 174] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6850256618980335e+38 / 1.6947377057948597e+38 | [NPY](tensors/0000685.npy) |
| 686 | `model.layers.17.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 174] | torch.int64 → int64 | 0.0 / 173.0 / 86.5 / 50.22864388639879 | [NPY](tensors/0000686.npy) |
| 687 | `model.layers.17.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 688 | `model.layers.17.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 689 | `model.layers.17.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8449686751968559 / 0.8475634832262998 | [NPY](tensors/0000689.npy) |
| 690 | `model.layers.17.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11834632235160365 / 0.6025126921634434 | [NPY](tensors/0000690.npy) |
| 691 | `model.layers.17.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 692 | `model.layers.17.self_attn.q_proj` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -124.5 / 87.0 / 0.04068461955354893 / 2.7416266632044977 | [NPY](tensors/0000692.npy) |
| 693 | `model.layers.17.self_attn.q_proj` | 0 | `output` | [1, 174, 4096] | torch.bfloat16 → float32 | -17.0 / 19.25 / 0.013163774205481631 / 1.5744590214123162 | [NPY](tensors/0000693.npy) |
| 694 | `model.layers.17.self_attn.k_proj` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -124.5 / 87.0 / 0.04068461955354893 / 2.7416266632044977 | [NPY](tensors/0000694.npy) |
| 695 | `model.layers.17.self_attn.k_proj` | 0 | `output` | [1, 174, 512] | torch.bfloat16 → float32 | -68.0 / 40.0 / -0.056144682947417784 / 4.80292275644836 | [NPY](tensors/0000695.npy) |
| 696 | `model.layers.17.self_attn.v_proj` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -124.5 / 87.0 / 0.04068461955354893 / 2.7416266632044977 | [NPY](tensors/0000696.npy) |
| 697 | `model.layers.17.self_attn.v_proj` | 0 | `output` | [1, 174, 512] | torch.bfloat16 → float32 | -19.5 / 21.75 / 0.12073642495034755 / 3.047283578913356 | [NPY](tensors/0000697.npy) |
| 698 | `model.layers.17.self_attn.o_proj` | 0 | `input.args[0]` | [1, 174, 4096] | torch.bfloat16 → float32 | -9.875 / 10.9375 / 0.06342436699974471 / 1.2311290546243359 | [NPY](tensors/0000698.npy) |
| 699 | `model.layers.17.self_attn.o_proj` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -1512.0 / 1552.0 / 0.28267517929960945 / 20.532419784837863 | [NPY](tensors/0000699.npy) |
| 700 | `model.layers.17.self_attn` | 0 | `output[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -1512.0 / 1552.0 / 0.28267517929960945 / 20.532419784837863 | [NPY](tensors/0000700.npy) |
| 701 | `model.layers.17.self_attn` | 0 | `output[1]` | [1, 64, 174, 174] | torch.bfloat16 → float32 | 0.0 / 0.984375 / 0.0040831142482383575 / 0.027552607212827013 | [NPY](tensors/0000701.npy) |
| 702 | `model.layers.17.post_attention_layernorm` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -41216.0 / 1824.0 / 0.5435805004066282 / 93.65293145185845 | [NPY](tensors/0000702.npy) |
| 703 | `model.layers.17.post_attention_layernorm` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -41.75 / 9.1875 / 0.008930437476166057 / 0.9501097713849659 | [NPY](tensors/0000703.npy) |
| 704 | `model.layers.17.mlp` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -41.75 / 9.1875 / 0.008930437476166057 / 0.9501097713849659 | [NPY](tensors/0000704.npy) |
| 705 | `model.layers.17.mlp.experts` | 0 | `input.args[0]` | [174, 2880] | torch.bfloat16 → float32 | -41.75 / 9.1875 / 0.008930437476166057 / 0.9501097713849659 | [NPY](tensors/0000705.npy) |
| 706 | `model.layers.17.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 707 | `model.layers.17.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 708 | `model.layers.17.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 709 | `model.layers.17.mlp.experts` | 0 | `output` | [174, 2880] | torch.bfloat16 → float32 | -1184.0 / 40448.0 / -0.08900301158047574 / 68.45630799397921 | [NPY](tensors/0000709.npy) |
| 710 | `model.layers.17.mlp` | 0 | `output[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -1184.0 / 40448.0 / -0.08900301158047574 / 68.45630799397921 | [NPY](tensors/0000710.npy) |
| 711 | `model.layers.17.mlp` | 0 | `output[1]` | [174, 32] | torch.bfloat16 → float32 | -4.90625 / 3.140625 / -0.20607247708857745 / 0.9531091574958914 | [NPY](tensors/0000711.npy) |
| 712 | `model.layers.17` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -2416.0 / 2496.0 / 0.4548122064972899 / 98.64950687309802 | [NPY](tensors/0000712.npy) |

## Layer 0018

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 713 | `model.layers.18` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -2416.0 / 2496.0 / 0.4548122064972899 / 98.64950687309802 | [NPY](tensors/0000713.npy) |
| 714 | `model.layers.18` | 0 | `input.kwargs['attention_mask']` | [1, 1, 174, 174] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.8060483674001114e+38 / 1.6911081947706832e+38 | [NPY](tensors/0000714.npy) |
| 715 | `model.layers.18` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8449686751968559 / 0.8475634832262998 | [NPY](tensors/0000715.npy) |
| 716 | `model.layers.18` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11834632235160365 / 0.6025126921634434 | [NPY](tensors/0000716.npy) |
| 717 | `model.layers.18` | 0 | `input.kwargs['position_ids']` | [1, 174] | torch.int64 → int64 | 0.0 / 173.0 / 86.5 / 50.22864388639879 | [NPY](tensors/0000717.npy) |
| 718 | `model.layers.18` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 719 | `model.layers.18` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 720 | `model.layers.18` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 721 | `model.layers.18.input_layernorm` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -2416.0 / 2496.0 / 0.4548122064972899 / 98.64950687309802 | [NPY](tensors/0000721.npy) |
| 722 | `model.layers.18.input_layernorm` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -45.5 / 39.0 / 0.01954129707367941 / 1.6009022835391393 | [NPY](tensors/0000722.npy) |
| 723 | `model.layers.18.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 174, 2880] | torch.bfloat16 → float32 | -45.5 / 39.0 / 0.01954129707367941 / 1.6009022835391393 | [NPY](tensors/0000723.npy) |
| 724 | `model.layers.18.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 174, 174] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.8060483674001114e+38 / 1.6911081947706832e+38 | [NPY](tensors/0000724.npy) |
| 725 | `model.layers.18.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 174] | torch.int64 → int64 | 0.0 / 173.0 / 86.5 / 50.22864388639879 | [NPY](tensors/0000725.npy) |
| 726 | `model.layers.18.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 727 | `model.layers.18.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 728 | `model.layers.18.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8449686751968559 / 0.8475634832262998 | [NPY](tensors/0000728.npy) |
| 729 | `model.layers.18.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11834632235160365 / 0.6025126921634434 | [NPY](tensors/0000729.npy) |
| 730 | `model.layers.18.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 731 | `model.layers.18.self_attn.q_proj` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -45.5 / 39.0 / 0.01954129707367941 / 1.6009022835391393 | [NPY](tensors/0000731.npy) |
| 732 | `model.layers.18.self_attn.q_proj` | 0 | `output` | [1, 174, 4096] | torch.bfloat16 → float32 | -25.5 / 31.25 / 0.12118011105015064 / 1.842387983381985 | [NPY](tensors/0000732.npy) |
| 733 | `model.layers.18.self_attn.k_proj` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -45.5 / 39.0 / 0.01954129707367941 / 1.6009022835391393 | [NPY](tensors/0000733.npy) |
| 734 | `model.layers.18.self_attn.k_proj` | 0 | `output` | [1, 174, 512] | torch.bfloat16 → float32 | -17.625 / 47.75 / 0.12084611063159402 / 2.254178207355524 | [NPY](tensors/0000734.npy) |
| 735 | `model.layers.18.self_attn.v_proj` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -45.5 / 39.0 / 0.01954129707367941 / 1.6009022835391393 | [NPY](tensors/0000735.npy) |
| 736 | `model.layers.18.self_attn.v_proj` | 0 | `output` | [1, 174, 512] | torch.bfloat16 → float32 | -24.5 / 23.375 / -0.2736992483166443 / 4.286700337800879 | [NPY](tensors/0000736.npy) |
| 737 | `model.layers.18.self_attn.o_proj` | 0 | `input.args[0]` | [1, 174, 4096] | torch.bfloat16 → float32 | -17.875 / 20.375 / -0.14509681372422573 / 1.842750800226578 | [NPY](tensors/0000737.npy) |
| 738 | `model.layers.18.self_attn.o_proj` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -464.0 / 644.0 / -0.41187186318343816 / 20.199484147067007 | [NPY](tensors/0000738.npy) |
| 739 | `model.layers.18.self_attn` | 0 | `output[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -464.0 / 644.0 / -0.41187186318343816 / 20.199484147067007 | [NPY](tensors/0000739.npy) |
| 740 | `model.layers.18.self_attn` | 0 | `output[1]` | [1, 64, 174, 174] | torch.bfloat16 → float32 | 0.0 / 0.99609375 / 0.002634044805918062 / 0.022445122803831825 | [NPY](tensors/0000740.npy) |
| 741 | `model.layers.18.post_attention_layernorm` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -2352.0 / 2448.0 / 0.04301790576023769 / 104.23568373462051 | [NPY](tensors/0000741.npy) |
| 742 | `model.layers.18.post_attention_layernorm` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -7.75 / 12.0 / 0.001600796761202934 / 0.9142327495548556 | [NPY](tensors/0000742.npy) |
| 743 | `model.layers.18.mlp` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -7.75 / 12.0 / 0.001600796761202934 / 0.9142327495548556 | [NPY](tensors/0000743.npy) |
| 744 | `model.layers.18.mlp.experts` | 0 | `input.args[0]` | [174, 2880] | torch.bfloat16 → float32 | -7.75 / 12.0 / 0.001600796761202934 / 0.9142327495548556 | [NPY](tensors/0000744.npy) |
| 745 | `model.layers.18.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 746 | `model.layers.18.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 747 | `model.layers.18.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 748 | `model.layers.18.mlp.experts` | 0 | `output` | [174, 2880] | torch.bfloat16 → float32 | -2080.0 / 2800.0 / 0.25851033315500227 / 57.446053571624134 | [NPY](tensors/0000748.npy) |
| 749 | `model.layers.18.mlp` | 0 | `output[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -2080.0 / 2800.0 / 0.25851033315500227 / 57.446053571624134 | [NPY](tensors/0000749.npy) |
| 750 | `model.layers.18.mlp` | 0 | `output[1]` | [174, 32] | torch.bfloat16 → float32 | -4.875 / 2.296875 / -0.3411833828893201 / 1.0332046079191275 | [NPY](tensors/0000750.npy) |
| 751 | `model.layers.18` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -4128.0 / 4288.0 / 0.3011361893109435 / 146.77954387663922 | [NPY](tensors/0000751.npy) |

## Layer 0019

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 752 | `model.layers.19` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -4128.0 / 4288.0 / 0.3011361893109435 / 146.77954387663922 | [NPY](tensors/0000752.npy) |
| 753 | `model.layers.19` | 0 | `input.kwargs['attention_mask']` | [1, 1, 174, 174] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6850256618980335e+38 / 1.6947377057948597e+38 | [NPY](tensors/0000753.npy) |
| 754 | `model.layers.19` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8449686751968559 / 0.8475634832262998 | [NPY](tensors/0000754.npy) |
| 755 | `model.layers.19` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11834632235160365 / 0.6025126921634434 | [NPY](tensors/0000755.npy) |
| 756 | `model.layers.19` | 0 | `input.kwargs['position_ids']` | [1, 174] | torch.int64 → int64 | 0.0 / 173.0 / 86.5 / 50.22864388639879 | [NPY](tensors/0000756.npy) |
| 757 | `model.layers.19` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 758 | `model.layers.19` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 759 | `model.layers.19` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 760 | `model.layers.19.input_layernorm` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -4128.0 / 4288.0 / 0.3011361893109435 / 146.77954387663922 | [NPY](tensors/0000760.npy) |
| 761 | `model.layers.19.input_layernorm` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -78.0 / 42.0 / 0.01169035674511701 / 1.8463190274399721 | [NPY](tensors/0000761.npy) |
| 762 | `model.layers.19.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 174, 2880] | torch.bfloat16 → float32 | -78.0 / 42.0 / 0.01169035674511701 / 1.8463190274399721 | [NPY](tensors/0000762.npy) |
| 763 | `model.layers.19.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 174, 174] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6850256618980335e+38 / 1.6947377057948597e+38 | [NPY](tensors/0000763.npy) |
| 764 | `model.layers.19.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 174] | torch.int64 → int64 | 0.0 / 173.0 / 86.5 / 50.22864388639879 | [NPY](tensors/0000764.npy) |
| 765 | `model.layers.19.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 766 | `model.layers.19.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 767 | `model.layers.19.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8449686751968559 / 0.8475634832262998 | [NPY](tensors/0000767.npy) |
| 768 | `model.layers.19.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11834632235160365 / 0.6025126921634434 | [NPY](tensors/0000768.npy) |
| 769 | `model.layers.19.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 770 | `model.layers.19.self_attn.q_proj` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -78.0 / 42.0 / 0.01169035674511701 / 1.8463190274399721 | [NPY](tensors/0000770.npy) |
| 771 | `model.layers.19.self_attn.q_proj` | 0 | `output` | [1, 174, 4096] | torch.bfloat16 → float32 | -15.0 / 24.5 / -0.0383938390252255 / 1.299820255909154 | [NPY](tensors/0000771.npy) |
| 772 | `model.layers.19.self_attn.k_proj` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -78.0 / 42.0 / 0.01169035674511701 / 1.8463190274399721 | [NPY](tensors/0000772.npy) |
| 773 | `model.layers.19.self_attn.k_proj` | 0 | `output` | [1, 174, 512] | torch.bfloat16 → float32 | -72.5 / 71.0 / -0.11569334020645454 / 6.834209763599595 | [NPY](tensors/0000773.npy) |
| 774 | `model.layers.19.self_attn.v_proj` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -78.0 / 42.0 / 0.01169035674511701 / 1.8463190274399721 | [NPY](tensors/0000774.npy) |
| 775 | `model.layers.19.self_attn.v_proj` | 0 | `output` | [1, 174, 512] | torch.bfloat16 → float32 | -15.9375 / 14.375 / -0.03229017188537052 / 3.1606204723121896 | [NPY](tensors/0000775.npy) |
| 776 | `model.layers.19.self_attn.o_proj` | 0 | `input.args[0]` | [1, 174, 4096] | torch.bfloat16 → float32 | -10.6875 / 11.125 / -0.01403909498863847 / 0.8907396118278081 | [NPY](tensors/0000776.npy) |
| 777 | `model.layers.19.self_attn.o_proj` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -2160.0 / 1920.0 / -0.6194589016709291 / 43.859234206718774 | [NPY](tensors/0000777.npy) |
| 778 | `model.layers.19.self_attn` | 0 | `output[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -2160.0 / 1920.0 / -0.6194589016709291 / 43.859234206718774 | [NPY](tensors/0000778.npy) |
| 779 | `model.layers.19.self_attn` | 0 | `output[1]` | [1, 64, 174, 174] | torch.bfloat16 → float32 | 0.0 / 0.9765625 / 0.0020382964615594814 / 0.012680618542778993 | [NPY](tensors/0000779.npy) |
| 780 | `model.layers.19.post_attention_layernorm` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -3568.0 / 3344.0 / -0.31803744500015285 / 126.43981527989433 | [NPY](tensors/0000780.npy) |
| 781 | `model.layers.19.post_attention_layernorm` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -7.15625 / 16.75 / 0.00025940270449771136 / 0.9782673753085918 | [NPY](tensors/0000781.npy) |
| 782 | `model.layers.19.mlp` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -7.15625 / 16.75 / 0.00025940270449771136 / 0.9782673753085918 | [NPY](tensors/0000782.npy) |
| 783 | `model.layers.19.mlp.experts` | 0 | `input.args[0]` | [174, 2880] | torch.bfloat16 → float32 | -7.15625 / 16.75 / 0.00025940270449771136 / 0.9782673753085918 | [NPY](tensors/0000783.npy) |
| 784 | `model.layers.19.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 785 | `model.layers.19.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 786 | `model.layers.19.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 787 | `model.layers.19.mlp.experts` | 0 | `output` | [174, 2880] | torch.bfloat16 → float32 | -2432.0 / 2528.0 / 0.31197363505113784 / 85.12544674483323 | [NPY](tensors/0000787.npy) |
| 788 | `model.layers.19.mlp` | 0 | `output[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -2432.0 / 2528.0 / 0.31197363505113784 / 85.12544674483323 | [NPY](tensors/0000788.npy) |
| 789 | `model.layers.19.mlp` | 0 | `output[1]` | [174, 32] | torch.bfloat16 → float32 | -6.25 / 2.984375 / -0.29000882992799254 / 1.4164986042849528 | [NPY](tensors/0000789.npy) |
| 790 | `model.layers.19` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -4960.0 / 4608.0 / -0.006245062329912256 / 186.49730089274243 | [NPY](tensors/0000790.npy) |

## Layer 0020

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 791 | `model.layers.20` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -4960.0 / 4608.0 / -0.006245062329912256 / 186.49730089274243 | [NPY](tensors/0000791.npy) |
| 792 | `model.layers.20` | 0 | `input.kwargs['attention_mask']` | [1, 1, 174, 174] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.8060483674001114e+38 / 1.6911081947706832e+38 | [NPY](tensors/0000792.npy) |
| 793 | `model.layers.20` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8449686751968559 / 0.8475634832262998 | [NPY](tensors/0000793.npy) |
| 794 | `model.layers.20` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11834632235160365 / 0.6025126921634434 | [NPY](tensors/0000794.npy) |
| 795 | `model.layers.20` | 0 | `input.kwargs['position_ids']` | [1, 174] | torch.int64 → int64 | 0.0 / 173.0 / 86.5 / 50.22864388639879 | [NPY](tensors/0000795.npy) |
| 796 | `model.layers.20` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 797 | `model.layers.20` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 798 | `model.layers.20` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 799 | `model.layers.20.input_layernorm` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -4960.0 / 4608.0 / -0.006245062329912256 / 186.49730089274243 | [NPY](tensors/0000799.npy) |
| 800 | `model.layers.20.input_layernorm` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -41.5 / 39.0 / 0.008327834516059545 / 1.5337255354979562 | [NPY](tensors/0000800.npy) |
| 801 | `model.layers.20.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 174, 2880] | torch.bfloat16 → float32 | -41.5 / 39.0 / 0.008327834516059545 / 1.5337255354979562 | [NPY](tensors/0000801.npy) |
| 802 | `model.layers.20.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 174, 174] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.8060483674001114e+38 / 1.6911081947706832e+38 | [NPY](tensors/0000802.npy) |
| 803 | `model.layers.20.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 174] | torch.int64 → int64 | 0.0 / 173.0 / 86.5 / 50.22864388639879 | [NPY](tensors/0000803.npy) |
| 804 | `model.layers.20.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 805 | `model.layers.20.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 806 | `model.layers.20.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8449686751968559 / 0.8475634832262998 | [NPY](tensors/0000806.npy) |
| 807 | `model.layers.20.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11834632235160365 / 0.6025126921634434 | [NPY](tensors/0000807.npy) |
| 808 | `model.layers.20.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 809 | `model.layers.20.self_attn.q_proj` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -41.5 / 39.0 / 0.008327834516059545 / 1.5337255354979562 | [NPY](tensors/0000809.npy) |
| 810 | `model.layers.20.self_attn.q_proj` | 0 | `output` | [1, 174, 4096] | torch.bfloat16 → float32 | -20.375 / 20.625 / 0.04513382769589784 / 1.235380758485301 | [NPY](tensors/0000810.npy) |
| 811 | `model.layers.20.self_attn.k_proj` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -41.5 / 39.0 / 0.008327834516059545 / 1.5337255354979562 | [NPY](tensors/0000811.npy) |
| 812 | `model.layers.20.self_attn.k_proj` | 0 | `output` | [1, 174, 512] | torch.bfloat16 → float32 | -27.0 / 37.0 / -0.10515811850969818 / 2.2321713903117444 | [NPY](tensors/0000812.npy) |
| 813 | `model.layers.20.self_attn.v_proj` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -41.5 / 39.0 / 0.008327834516059545 / 1.5337255354979562 | [NPY](tensors/0000813.npy) |
| 814 | `model.layers.20.self_attn.v_proj` | 0 | `output` | [1, 174, 512] | torch.bfloat16 → float32 | -22.5 / 20.5 / -0.005504285124526626 / 3.9375501101405272 | [NPY](tensors/0000814.npy) |
| 815 | `model.layers.20.self_attn.o_proj` | 0 | `input.args[0]` | [1, 174, 4096] | torch.bfloat16 → float32 | -17.5 / 17.5 / -0.014287114436228878 / 1.2771801341999525 | [NPY](tensors/0000815.npy) |
| 816 | `model.layers.20.self_attn.o_proj` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -1032.0 / 1112.0 / -0.19410012759515685 / 24.860093995741178 | [NPY](tensors/0000816.npy) |
| 817 | `model.layers.20.self_attn` | 0 | `output[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -1032.0 / 1112.0 / -0.19410012759515685 / 24.860093995741178 | [NPY](tensors/0000817.npy) |
| 818 | `model.layers.20.self_attn` | 0 | `output[1]` | [1, 64, 174, 174] | torch.bfloat16 → float32 | 0.0 / 0.9921875 / 0.002248892299940712 / 0.0187552689630056 | [NPY](tensors/0000818.npy) |
| 819 | `model.layers.20.post_attention_layernorm` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -4864.0 / 4832.0 / -0.20020562265720102 / 191.48318420136238 | [NPY](tensors/0000819.npy) |
| 820 | `model.layers.20.post_attention_layernorm` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -6.96875 / 15.4375 / -0.0010249966415332803 / 0.9319123540352243 | [NPY](tensors/0000820.npy) |
| 821 | `model.layers.20.mlp` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -6.96875 / 15.4375 / -0.0010249966415332803 / 0.9319123540352243 | [NPY](tensors/0000821.npy) |
| 822 | `model.layers.20.mlp.experts` | 0 | `input.args[0]` | [174, 2880] | torch.bfloat16 → float32 | -6.96875 / 15.4375 / -0.0010249966415332803 / 0.9319123540352243 | [NPY](tensors/0000822.npy) |
| 823 | `model.layers.20.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 824 | `model.layers.20.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 825 | `model.layers.20.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 826 | `model.layers.20.mlp.experts` | 0 | `output` | [174, 2880] | torch.bfloat16 → float32 | -5888.0 / 6816.0 / 0.43573721190521997 / 84.89967920101617 | [NPY](tensors/0000826.npy) |
| 827 | `model.layers.20.mlp` | 0 | `output[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -5888.0 / 6816.0 / 0.43573721190521997 / 84.89967920101617 | [NPY](tensors/0000827.npy) |
| 828 | `model.layers.20.mlp` | 0 | `output[1]` | [174, 32] | torch.bfloat16 → float32 | -5.28125 / 3.84375 / -0.17678090895729504 / 1.187741887581707 | [NPY](tensors/0000828.npy) |
| 829 | `model.layers.20` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -9152.0 / 10240.0 / 0.236007764969749 / 254.07997493531096 | [NPY](tensors/0000829.npy) |

## Layer 0021

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 830 | `model.layers.21` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -9152.0 / 10240.0 / 0.236007764969749 / 254.07997493531096 | [NPY](tensors/0000830.npy) |
| 831 | `model.layers.21` | 0 | `input.kwargs['attention_mask']` | [1, 1, 174, 174] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6850256618980335e+38 / 1.6947377057948597e+38 | [NPY](tensors/0000831.npy) |
| 832 | `model.layers.21` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8449686751968559 / 0.8475634832262998 | [NPY](tensors/0000832.npy) |
| 833 | `model.layers.21` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11834632235160365 / 0.6025126921634434 | [NPY](tensors/0000833.npy) |
| 834 | `model.layers.21` | 0 | `input.kwargs['position_ids']` | [1, 174] | torch.int64 → int64 | 0.0 / 173.0 / 86.5 / 50.22864388639879 | [NPY](tensors/0000834.npy) |
| 835 | `model.layers.21` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 836 | `model.layers.21` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 837 | `model.layers.21` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 838 | `model.layers.21.input_layernorm` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -9152.0 / 10240.0 / 0.236007764969749 / 254.07997493531096 | [NPY](tensors/0000838.npy) |
| 839 | `model.layers.21.input_layernorm` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -75.5 / 63.5 / 0.0048440576265750416 / 1.8120918204773153 | [NPY](tensors/0000839.npy) |
| 840 | `model.layers.21.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 174, 2880] | torch.bfloat16 → float32 | -75.5 / 63.5 / 0.0048440576265750416 / 1.8120918204773153 | [NPY](tensors/0000840.npy) |
| 841 | `model.layers.21.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 174, 174] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6850256618980335e+38 / 1.6947377057948597e+38 | [NPY](tensors/0000841.npy) |
| 842 | `model.layers.21.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 174] | torch.int64 → int64 | 0.0 / 173.0 / 86.5 / 50.22864388639879 | [NPY](tensors/0000842.npy) |
| 843 | `model.layers.21.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 844 | `model.layers.21.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 845 | `model.layers.21.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8449686751968559 / 0.8475634832262998 | [NPY](tensors/0000845.npy) |
| 846 | `model.layers.21.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11834632235160365 / 0.6025126921634434 | [NPY](tensors/0000846.npy) |
| 847 | `model.layers.21.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 848 | `model.layers.21.self_attn.q_proj` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -75.5 / 63.5 / 0.0048440576265750416 / 1.8120918204773153 | [NPY](tensors/0000848.npy) |
| 849 | `model.layers.21.self_attn.q_proj` | 0 | `output` | [1, 174, 4096] | torch.bfloat16 → float32 | -19.5 / 33.5 / 0.023681354447975977 / 1.1445006637302952 | [NPY](tensors/0000849.npy) |
| 850 | `model.layers.21.self_attn.k_proj` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -75.5 / 63.5 / 0.0048440576265750416 / 1.8120918204773153 | [NPY](tensors/0000850.npy) |
| 851 | `model.layers.21.self_attn.k_proj` | 0 | `output` | [1, 174, 512] | torch.bfloat16 → float32 | -101.0 / 99.0 / -0.153950823032051 / 7.863700566269562 | [NPY](tensors/0000851.npy) |
| 852 | `model.layers.21.self_attn.v_proj` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -75.5 / 63.5 / 0.0048440576265750416 / 1.8120918204773153 | [NPY](tensors/0000852.npy) |
| 853 | `model.layers.21.self_attn.v_proj` | 0 | `output` | [1, 174, 512] | torch.bfloat16 → float32 | -21.5 / 20.75 / -0.011793120839129919 / 3.10108744543156 | [NPY](tensors/0000853.npy) |
| 854 | `model.layers.21.self_attn.o_proj` | 0 | `input.args[0]` | [1, 174, 4096] | torch.bfloat16 → float32 | -16.25 / 13.5625 / 0.0038974141886334458 / 0.6475920388627924 | [NPY](tensors/0000854.npy) |
| 855 | `model.layers.21.self_attn.o_proj` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -5184.0 / 4736.0 / -0.5647395993315283 / 84.54034974686255 | [NPY](tensors/0000855.npy) |
| 856 | `model.layers.21.self_attn` | 0 | `output[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -5184.0 / 4736.0 / -0.5647395993315283 / 84.54034974686255 | [NPY](tensors/0000856.npy) |
| 857 | `model.layers.21.self_attn` | 0 | `output[1]` | [1, 64, 174, 174] | torch.bfloat16 → float32 | 0.0 / 0.92578125 / 0.0019870876076172996 / 0.00979143725948482 | [NPY](tensors/0000857.npy) |
| 858 | `model.layers.21.post_attention_layernorm` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -5888.0 / 6080.0 / -0.3294466446376243 / 203.8101951295947 | [NPY](tensors/0000858.npy) |
| 859 | `model.layers.21.post_attention_layernorm` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -8.6875 / 22.75 / -0.0005623671920235016 / 1.063290022905431 | [NPY](tensors/0000859.npy) |
| 860 | `model.layers.21.mlp` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -8.6875 / 22.75 / -0.0005623671920235016 / 1.063290022905431 | [NPY](tensors/0000860.npy) |
| 861 | `model.layers.21.mlp.experts` | 0 | `input.args[0]` | [174, 2880] | torch.bfloat16 → float32 | -8.6875 / 22.75 / -0.0005623671920235016 / 1.063290022905431 | [NPY](tensors/0000861.npy) |
| 862 | `model.layers.21.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 863 | `model.layers.21.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 864 | `model.layers.21.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 865 | `model.layers.21.mlp.experts` | 0 | `output` | [174, 2880] | torch.bfloat16 → float32 | -5792.0 / 5664.0 / -0.9219765559619109 / 159.39772621725467 | [NPY](tensors/0000865.npy) |
| 866 | `model.layers.21.mlp` | 0 | `output[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -5792.0 / 5664.0 / -0.9219765559619109 / 159.39772621725467 | [NPY](tensors/0000866.npy) |
| 867 | `model.layers.21.mlp` | 0 | `output[1]` | [174, 32] | torch.bfloat16 → float32 | -5.59375 / 4.375 / -0.2205881962830993 / 1.5299339483922272 | [NPY](tensors/0000867.npy) |
| 868 | `model.layers.21` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -9216.0 / 9600.0 / -1.251197271724618 / 317.4203325998318 | [NPY](tensors/0000868.npy) |

## Layer 0022

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 869 | `model.layers.22` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -9216.0 / 9600.0 / -1.251197271724618 / 317.4203325998318 | [NPY](tensors/0000869.npy) |
| 870 | `model.layers.22` | 0 | `input.kwargs['attention_mask']` | [1, 1, 174, 174] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.8060483674001114e+38 / 1.6911081947706832e+38 | [NPY](tensors/0000870.npy) |
| 871 | `model.layers.22` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8449686751968559 / 0.8475634832262998 | [NPY](tensors/0000871.npy) |
| 872 | `model.layers.22` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11834632235160365 / 0.6025126921634434 | [NPY](tensors/0000872.npy) |
| 873 | `model.layers.22` | 0 | `input.kwargs['position_ids']` | [1, 174] | torch.int64 → int64 | 0.0 / 173.0 / 86.5 / 50.22864388639879 | [NPY](tensors/0000873.npy) |
| 874 | `model.layers.22` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 875 | `model.layers.22` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 876 | `model.layers.22` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 877 | `model.layers.22.input_layernorm` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -9216.0 / 9600.0 / -1.251197271724618 / 317.4203325998318 | [NPY](tensors/0000877.npy) |
| 878 | `model.layers.22.input_layernorm` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -43.0 / 49.0 / -9.925858299622588e-05 / 1.7220133379025864 | [NPY](tensors/0000878.npy) |
| 879 | `model.layers.22.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 174, 2880] | torch.bfloat16 → float32 | -43.0 / 49.0 / -9.925858299622588e-05 / 1.7220133379025864 | [NPY](tensors/0000879.npy) |
| 880 | `model.layers.22.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 174, 174] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.8060483674001114e+38 / 1.6911081947706832e+38 | [NPY](tensors/0000880.npy) |
| 881 | `model.layers.22.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 174] | torch.int64 → int64 | 0.0 / 173.0 / 86.5 / 50.22864388639879 | [NPY](tensors/0000881.npy) |
| 882 | `model.layers.22.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 883 | `model.layers.22.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 884 | `model.layers.22.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8449686751968559 / 0.8475634832262998 | [NPY](tensors/0000884.npy) |
| 885 | `model.layers.22.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11834632235160365 / 0.6025126921634434 | [NPY](tensors/0000885.npy) |
| 886 | `model.layers.22.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 887 | `model.layers.22.self_attn.q_proj` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -43.0 / 49.0 / -9.925858299622588e-05 / 1.7220133379025864 | [NPY](tensors/0000887.npy) |
| 888 | `model.layers.22.self_attn.q_proj` | 0 | `output` | [1, 174, 4096] | torch.bfloat16 → float32 | -40.25 / 31.5 / -0.05260292342937573 / 2.46955895487202 | [NPY](tensors/0000888.npy) |
| 889 | `model.layers.22.self_attn.k_proj` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -43.0 / 49.0 / -9.925858299622588e-05 / 1.7220133379025864 | [NPY](tensors/0000889.npy) |
| 890 | `model.layers.22.self_attn.k_proj` | 0 | `output` | [1, 174, 512] | torch.bfloat16 → float32 | -32.75 / 9.1875 / -0.05384953467753427 / 1.3718784290673587 | [NPY](tensors/0000890.npy) |
| 891 | `model.layers.22.self_attn.v_proj` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -43.0 / 49.0 / -9.925858299622588e-05 / 1.7220133379025864 | [NPY](tensors/0000891.npy) |
| 892 | `model.layers.22.self_attn.v_proj` | 0 | `output` | [1, 174, 512] | torch.bfloat16 → float32 | -26.75 / 26.25 / -0.046963598707626605 / 4.380552832572213 | [NPY](tensors/0000892.npy) |
| 893 | `model.layers.22.self_attn.o_proj` | 0 | `input.args[0]` | [1, 174, 4096] | torch.bfloat16 → float32 | -19.875 / 13.8125 / -0.031944194305913116 / 1.489114321010255 | [NPY](tensors/0000893.npy) |
| 894 | `model.layers.22.self_attn.o_proj` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -2144.0 / 1432.0 / -0.386709516545898 / 40.67218661494656 | [NPY](tensors/0000894.npy) |
| 895 | `model.layers.22.self_attn` | 0 | `output[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -2144.0 / 1432.0 / -0.386709516545898 / 40.67218661494656 | [NPY](tensors/0000895.npy) |
| 896 | `model.layers.22.self_attn` | 0 | `output[1]` | [1, 64, 174, 174] | torch.bfloat16 → float32 | 0.0 / 0.93359375 / 0.002289993179365899 / 0.01938784901729301 | [NPY](tensors/0000896.npy) |
| 897 | `model.layers.22.post_attention_layernorm` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -9984.0 / 10304.0 / -1.6380889152049412 / 330.7281963940585 | [NPY](tensors/0000897.npy) |
| 898 | `model.layers.22.post_attention_layernorm` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -14.125 / 17.75 / -0.00907159979344556 / 0.9528738146435856 | [NPY](tensors/0000898.npy) |
| 899 | `model.layers.22.mlp` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -14.125 / 17.75 / -0.00907159979344556 / 0.9528738146435856 | [NPY](tensors/0000899.npy) |
| 900 | `model.layers.22.mlp.experts` | 0 | `input.args[0]` | [174, 2880] | torch.bfloat16 → float32 | -14.125 / 17.75 / -0.00907159979344556 / 0.9528738146435856 | [NPY](tensors/0000900.npy) |
| 901 | `model.layers.22.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 902 | `model.layers.22.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 903 | `model.layers.22.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 904 | `model.layers.22.mlp.experts` | 0 | `output` | [174, 2880] | torch.bfloat16 → float32 | -6624.0 / 6336.0 / 0.056486715789346706 / 156.03702712432943 | [NPY](tensors/0000904.npy) |
| 905 | `model.layers.22.mlp` | 0 | `output[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -6624.0 / 6336.0 / 0.056486715789346706 / 156.03702712432943 | [NPY](tensors/0000905.npy) |
| 906 | `model.layers.22.mlp` | 0 | `output[1]` | [174, 32] | torch.bfloat16 → float32 | -6.46875 / 4.75 / -0.1720120550572187 / 1.3843040155045019 | [NPY](tensors/0000906.npy) |
| 907 | `model.layers.22` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -12928.0 / 13952.0 / -1.5808884724194368 / 425.7010697672106 | [NPY](tensors/0000907.npy) |

## Layer 0023

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 908 | `model.layers.23` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -12928.0 / 13952.0 / -1.5808884724194368 / 425.7010697672106 | [NPY](tensors/0000908.npy) |
| 909 | `model.layers.23` | 0 | `input.kwargs['attention_mask']` | [1, 1, 174, 174] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6850256618980335e+38 / 1.6947377057948597e+38 | [NPY](tensors/0000909.npy) |
| 910 | `model.layers.23` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8449686751968559 / 0.8475634832262998 | [NPY](tensors/0000910.npy) |
| 911 | `model.layers.23` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11834632235160365 / 0.6025126921634434 | [NPY](tensors/0000911.npy) |
| 912 | `model.layers.23` | 0 | `input.kwargs['position_ids']` | [1, 174] | torch.int64 → int64 | 0.0 / 173.0 / 86.5 / 50.22864388639879 | [NPY](tensors/0000912.npy) |
| 913 | `model.layers.23` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 914 | `model.layers.23` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 915 | `model.layers.23` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 916 | `model.layers.23.input_layernorm` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -12928.0 / 13952.0 / -1.5808884724194368 / 425.7010697672106 | [NPY](tensors/0000916.npy) |
| 917 | `model.layers.23.input_layernorm` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -53.25 / 71.5 / 0.009228820871385731 / 1.7597860111439938 | [NPY](tensors/0000917.npy) |
| 918 | `model.layers.23.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 174, 2880] | torch.bfloat16 → float32 | -53.25 / 71.5 / 0.009228820871385731 / 1.7597860111439938 | [NPY](tensors/0000918.npy) |
| 919 | `model.layers.23.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 174, 174] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6850256618980335e+38 / 1.6947377057948597e+38 | [NPY](tensors/0000919.npy) |
| 920 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 174] | torch.int64 → int64 | 0.0 / 173.0 / 86.5 / 50.22864388639879 | [NPY](tensors/0000920.npy) |
| 921 | `model.layers.23.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 922 | `model.layers.23.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 923 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.8449686751968559 / 0.8475634832262998 | [NPY](tensors/0000923.npy) |
| 924 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 174, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.11834632235160365 / 0.6025126921634434 | [NPY](tensors/0000924.npy) |
| 925 | `model.layers.23.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 926 | `model.layers.23.self_attn.q_proj` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -53.25 / 71.5 / 0.009228820871385731 / 1.7597860111439938 | [NPY](tensors/0000926.npy) |
| 927 | `model.layers.23.self_attn.q_proj` | 0 | `output` | [1, 174, 4096] | torch.bfloat16 → float32 | -18.5 / 24.25 / 0.03184927980718667 / 1.607531895467666 | [NPY](tensors/0000927.npy) |
| 928 | `model.layers.23.self_attn.k_proj` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -53.25 / 71.5 / 0.009228820871385731 / 1.7597860111439938 | [NPY](tensors/0000928.npy) |
| 929 | `model.layers.23.self_attn.k_proj` | 0 | `output` | [1, 174, 512] | torch.bfloat16 → float32 | -82.5 / 59.0 / -0.07801261980718152 / 4.830221845305005 | [NPY](tensors/0000929.npy) |
| 930 | `model.layers.23.self_attn.v_proj` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -53.25 / 71.5 / 0.009228820871385731 / 1.7597860111439938 | [NPY](tensors/0000930.npy) |
| 931 | `model.layers.23.self_attn.v_proj` | 0 | `output` | [1, 174, 512] | torch.bfloat16 → float32 | -24.625 / 24.125 / 0.004791818816086341 / 3.1146776445307225 | [NPY](tensors/0000931.npy) |
| 932 | `model.layers.23.self_attn.o_proj` | 0 | `input.args[0]` | [1, 174, 4096] | torch.bfloat16 → float32 | -23.0 / 12.9375 / -0.004208435436297826 / 1.1268762717057863 | [NPY](tensors/0000932.npy) |
| 933 | `model.layers.23.self_attn.o_proj` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -6048.0 / 6240.0 / 2.7642994942907175 / 165.5740813821752 | [NPY](tensors/0000933.npy) |
| 934 | `model.layers.23.self_attn` | 0 | `output[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -6048.0 / 6240.0 / 2.7642994942907175 / 165.5740813821752 | [NPY](tensors/0000934.npy) |
| 935 | `model.layers.23.self_attn` | 0 | `output[1]` | [1, 64, 174, 174] | torch.bfloat16 → float32 | 0.0 / 0.9921875 / 0.002603487503951595 / 0.016630347195586453 | [NPY](tensors/0000935.npy) |
| 936 | `model.layers.23.post_attention_layernorm` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -10496.0 / 11200.0 / 1.18218274073887 / 374.6035717289141 | [NPY](tensors/0000936.npy) |
| 937 | `model.layers.23.post_attention_layernorm` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -47.25 / 18.375 / -0.014999684488750508 / 1.1865892974235088 | [NPY](tensors/0000937.npy) |
| 938 | `model.layers.23.mlp` | 0 | `input.args[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -47.25 / 18.375 / -0.014999684488750508 / 1.1865892974235088 | [NPY](tensors/0000938.npy) |
| 939 | `model.layers.23.mlp.experts` | 0 | `input.args[0]` | [174, 2880] | torch.bfloat16 → float32 | -47.25 / 18.375 / -0.014999684488750508 / 1.1865892974235088 | [NPY](tensors/0000939.npy) |
| 940 | `model.layers.23.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 941 | `model.layers.23.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 942 | `model.layers.23.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 943 | `model.layers.23.mlp.experts` | 0 | `output` | [174, 2880] | torch.bfloat16 → float32 | -4800.0 / 4704.0 / -1.4575357329952001 / 159.3796604965728 | [NPY](tensors/0000943.npy) |
| 944 | `model.layers.23.mlp` | 0 | `output[0]` | [1, 174, 2880] | torch.bfloat16 → float32 | -4800.0 / 4704.0 / -1.4575357329952001 / 159.3796604965728 | [NPY](tensors/0000944.npy) |
| 945 | `model.layers.23.mlp` | 0 | `output[1]` | [174, 32] | torch.bfloat16 → float32 | -7.28125 / 4.0 / 0.24869176437114848 / 2.3438089266778674 | [NPY](tensors/0000945.npy) |
| 946 | `model.layers.23` | 0 | `output` | [1, 174, 2880] | torch.bfloat16 → float32 | -10688.0 / 10880.0 / -0.2755838055568028 / 437.7624568706959 | [NPY](tensors/0000946.npy) |

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
