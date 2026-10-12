# Hook inspection: pre_action_full_prefix_replay

Status: **complete**. 90 full tensors; 117 records.

Input and output leaves are indexed separately. Call indices are local to each module. Module boundaries only; missing outputs are not reconstructed. Full values are in linked NPY files.

## Layer 0000

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | `model.layers.0` | 0 | `input.args[0]` | [1, 714, 2880] | torch.bfloat16 → float32 | -95.0 / 89.0 / -0.01396436620611782 / 2.7159210107022824 | [NPY](tensors/0000000.npy) |
| 1 | `model.layers.0` | 0 | `input.kwargs['attention_mask']` | [1, 1, 714, 714] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.835925747789775e+38 / 1.2529902205297064e+38 | [NPY](tensors/0000001.npy) |
| 2 | `model.layers.0` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 714, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7411219109037593 / 0.9062333078556434 | [NPY](tensors/0000002.npy) |
| 3 | `model.layers.0` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 714, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10502767491443618 / 0.6543104876572913 | [NPY](tensors/0000003.npy) |
| 4 | `model.layers.0` | 0 | `input.kwargs['position_ids']` | [1, 714] | torch.int64 → int64 | 0.0 / 713.0 / 356.5 / 206.11384394714165 | [NPY](tensors/0000004.npy) |
| 5 | `model.layers.0` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 6 | `model.layers.0` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 7 | `model.layers.0` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 8 | `model.layers.0.input_layernorm` | 0 | `input.args[0]` | [1, 714, 2880] | torch.bfloat16 → float32 | -95.0 / 89.0 / -0.01396436620611782 / 2.7159210107022824 | [NPY](tensors/0000008.npy) |
| 9 | `model.layers.0.input_layernorm` | 0 | `output` | [1, 714, 2880] | torch.bfloat16 → float32 | -30.25 / 15.0 / -0.0064264766157712296 / 0.7592488421513401 | [NPY](tensors/0000009.npy) |
| 10 | `model.layers.0.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 714, 2880] | torch.bfloat16 → float32 | -30.25 / 15.0 / -0.0064264766157712296 / 0.7592488421513401 | [NPY](tensors/0000010.npy) |
| 11 | `model.layers.0.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 714, 714] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -2.835925747789775e+38 / 1.2529902205297064e+38 | [NPY](tensors/0000011.npy) |
| 12 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 714] | torch.int64 → int64 | 0.0 / 713.0 / 356.5 / 206.11384394714165 | [NPY](tensors/0000012.npy) |
| 13 | `model.layers.0.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 14 | `model.layers.0.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 15 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 714, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7411219109037593 / 0.9062333078556434 | [NPY](tensors/0000015.npy) |
| 16 | `model.layers.0.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 714, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10502767491443618 / 0.6543104876572913 | [NPY](tensors/0000016.npy) |
| 17 | `model.layers.0.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 18 | `model.layers.0.self_attn.q_proj` | 0 | `input.args[0]` | [1, 714, 2880] | torch.bfloat16 → float32 | -30.25 / 15.0 / -0.0064264766157712296 / 0.7592488421513401 | [NPY](tensors/0000018.npy) |
| 19 | `model.layers.0.self_attn.q_proj` | 0 | `output` | [1, 714, 4096] | torch.bfloat16 → float32 | -9.5 / 14.0 / 0.017452482469633445 / 1.0257557120976855 | [NPY](tensors/0000019.npy) |
| 20 | `model.layers.0.self_attn.k_proj` | 0 | `input.args[0]` | [1, 714, 2880] | torch.bfloat16 → float32 | -30.25 / 15.0 / -0.0064264766157712296 / 0.7592488421513401 | [NPY](tensors/0000020.npy) |
| 21 | `model.layers.0.self_attn.k_proj` | 0 | `output` | [1, 714, 512] | torch.bfloat16 → float32 | -63.75 / 67.5 / 0.016521472313652644 / 5.734764361909026 | [NPY](tensors/0000021.npy) |
| 22 | `model.layers.0.self_attn.v_proj` | 0 | `input.args[0]` | [1, 714, 2880] | torch.bfloat16 → float32 | -30.25 / 15.0 / -0.0064264766157712296 / 0.7592488421513401 | [NPY](tensors/0000022.npy) |
| 23 | `model.layers.0.self_attn.v_proj` | 0 | `output` | [1, 714, 512] | torch.bfloat16 → float32 | -7.78125 / 9.0 / -0.01436272830994544 / 1.2025648680666778 | [NPY](tensors/0000023.npy) |
| 24 | `model.layers.0.self_attn.o_proj` | 0 | `input.args[0]` | [1, 714, 4096] | torch.bfloat16 → float32 | -7.03125 / 6.625 / -0.006300208414579514 / 0.5509274698858081 | [NPY](tensors/0000024.npy) |
| 25 | `model.layers.0.self_attn.o_proj` | 0 | `output` | [1, 714, 2880] | torch.bfloat16 → float32 | -51.0 / 57.25 / 0.027307463576942907 / 1.2270741405394632 | [NPY](tensors/0000025.npy) |
| 26 | `model.layers.0.self_attn` | 0 | `output[0]` | [1, 714, 2880] | torch.bfloat16 → float32 | -51.0 / 57.25 / 0.027307463576942907 / 1.2270741405394632 | [NPY](tensors/0000026.npy) |
| 27 | `model.layers.0.self_attn` | 0 | `output[1]` | [1, 64, 714, 714] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0005615029918772703 / 0.015267814451423604 | [NPY](tensors/0000027.npy) |
| 28 | `model.layers.0.post_attention_layernorm` | 0 | `input.args[0]` | [1, 714, 2880] | torch.bfloat16 → float32 | -90.5 / 71.0 / 0.013343147928961296 / 2.959046085874374 | [NPY](tensors/0000028.npy) |
| 29 | `model.layers.0.post_attention_layernorm` | 0 | `output` | [1, 714, 2880] | torch.bfloat16 → float32 | -6.5 / 3.828125 / 0.001708243207538189 / 0.3381830406751719 | [NPY](tensors/0000029.npy) |
| 30 | `model.layers.0.mlp` | 0 | `input.args[0]` | [1, 714, 2880] | torch.bfloat16 → float32 | -6.5 / 3.828125 / 0.001708243207538189 / 0.3381830406751719 | [NPY](tensors/0000030.npy) |
| 31 | `model.layers.0.mlp.experts` | 0 | `input.args[0]` | [714, 2880] | torch.bfloat16 → float32 | -6.5 / 3.828125 / 0.001708243207538189 / 0.3381830406751719 | [NPY](tensors/0000031.npy) |
| 32 | `model.layers.0.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 33 | `model.layers.0.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 34 | `model.layers.0.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 35 | `model.layers.0.mlp.experts` | 0 | `output` | [714, 2880] | torch.bfloat16 → float32 | -49.75 / 136.0 / 0.01805145463645644 / 0.8764341398240049 | [NPY](tensors/0000035.npy) |
| 36 | `model.layers.0.mlp` | 0 | `output[0]` | [1, 714, 2880] | torch.bfloat16 → float32 | -49.75 / 136.0 / 0.01805145463645644 / 0.8764341398240049 | [NPY](tensors/0000036.npy) |
| 37 | `model.layers.0.mlp` | 0 | `output[1]` | [714, 32] | torch.bfloat16 → float32 | -5.1875 / 3.84375 / -0.11146290028462556 / 0.9927731458137424 | [NPY](tensors/0000037.npy) |
| 38 | `model.layers.0` | 0 | `output` | [1, 714, 2880] | torch.bfloat16 → float32 | -86.0 / 157.0 / 0.031398777988815546 / 3.2467780903772527 | [NPY](tensors/0000038.npy) |

## Layer 0011

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 39 | `model.layers.11` | 0 | `input.args[0]` | [1, 714, 2880] | torch.bfloat16 → float32 | -41728.0 / 1096.0 / 0.4601912630557866 / 35.75767144772983 | [NPY](tensors/0000039.npy) |
| 40 | `model.layers.11` | 0 | `input.kwargs['attention_mask']` | [1, 1, 714, 714] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6923920732047232e+38 / 1.6947640324250779e+38 | [NPY](tensors/0000040.npy) |
| 41 | `model.layers.11` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 714, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7411219109037593 / 0.9062333078556434 | [NPY](tensors/0000041.npy) |
| 42 | `model.layers.11` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 714, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10502767491443618 / 0.6543104876572913 | [NPY](tensors/0000042.npy) |
| 43 | `model.layers.11` | 0 | `input.kwargs['position_ids']` | [1, 714] | torch.int64 → int64 | 0.0 / 713.0 / 356.5 / 206.11384394714165 | [NPY](tensors/0000043.npy) |
| 44 | `model.layers.11` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 45 | `model.layers.11` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 46 | `model.layers.11` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 47 | `model.layers.11.input_layernorm` | 0 | `input.args[0]` | [1, 714, 2880] | torch.bfloat16 → float32 | -41728.0 / 1096.0 / 0.4601912630557866 / 35.75767144772983 | [NPY](tensors/0000047.npy) |
| 48 | `model.layers.11.input_layernorm` | 0 | `output` | [1, 714, 2880] | torch.bfloat16 → float32 | -191.0 / 143.0 / 0.06060924476949997 / 3.1497160962022215 | [NPY](tensors/0000048.npy) |
| 49 | `model.layers.11.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 714, 2880] | torch.bfloat16 → float32 | -191.0 / 143.0 / 0.06060924476949997 / 3.1497160962022215 | [NPY](tensors/0000049.npy) |
| 50 | `model.layers.11.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 714, 714] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6923920732047232e+38 / 1.6947640324250779e+38 | [NPY](tensors/0000050.npy) |
| 51 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 714] | torch.int64 → int64 | 0.0 / 713.0 / 356.5 / 206.11384394714165 | [NPY](tensors/0000051.npy) |
| 52 | `model.layers.11.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 53 | `model.layers.11.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 54 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 714, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7411219109037593 / 0.9062333078556434 | [NPY](tensors/0000054.npy) |
| 55 | `model.layers.11.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 714, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10502767491443618 / 0.6543104876572913 | [NPY](tensors/0000055.npy) |
| 56 | `model.layers.11.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 57 | `model.layers.11.self_attn.q_proj` | 0 | `input.args[0]` | [1, 714, 2880] | torch.bfloat16 → float32 | -191.0 / 143.0 / 0.06060924476949997 / 3.1497160962022215 | [NPY](tensors/0000057.npy) |
| 58 | `model.layers.11.self_attn.q_proj` | 0 | `output` | [1, 714, 4096] | torch.bfloat16 → float32 | -13.0625 / 14.625 / 0.038333471495622315 / 1.329878596122706 | [NPY](tensors/0000058.npy) |
| 59 | `model.layers.11.self_attn.k_proj` | 0 | `input.args[0]` | [1, 714, 2880] | torch.bfloat16 → float32 | -191.0 / 143.0 / 0.06060924476949997 / 3.1497160962022215 | [NPY](tensors/0000059.npy) |
| 60 | `model.layers.11.self_attn.k_proj` | 0 | `output` | [1, 714, 512] | torch.bfloat16 → float32 | -41.25 / 51.5 / 0.09259774522938298 / 3.7293617915425514 | [NPY](tensors/0000060.npy) |
| 61 | `model.layers.11.self_attn.v_proj` | 0 | `input.args[0]` | [1, 714, 2880] | torch.bfloat16 → float32 | -191.0 / 143.0 / 0.06060924476949997 / 3.1497160962022215 | [NPY](tensors/0000061.npy) |
| 62 | `model.layers.11.self_attn.v_proj` | 0 | `output` | [1, 714, 512] | torch.bfloat16 → float32 | -16.0 / 22.125 / -0.004817033371449833 / 2.4605053425743364 | [NPY](tensors/0000062.npy) |
| 63 | `model.layers.11.self_attn.o_proj` | 0 | `input.args[0]` | [1, 714, 4096] | torch.bfloat16 → float32 | -11.4375 / 13.125 / -0.0008728012396783527 / 1.3869388644199938 | [NPY](tensors/0000063.npy) |
| 64 | `model.layers.11.self_attn.o_proj` | 0 | `output` | [1, 714, 2880] | torch.bfloat16 → float32 | -480.0 / 436.0 / -0.006323372687242393 / 5.399295365756746 | [NPY](tensors/0000064.npy) |
| 65 | `model.layers.11.self_attn` | 0 | `output[0]` | [1, 714, 2880] | torch.bfloat16 → float32 | -480.0 / 436.0 / -0.006323372687242393 / 5.399295365756746 | [NPY](tensors/0000065.npy) |
| 66 | `model.layers.11.self_attn` | 0 | `output[1]` | [1, 64, 714, 714] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0012313768371838862 / 0.011069499767431911 | [NPY](tensors/0000066.npy) |
| 67 | `model.layers.11.post_attention_layernorm` | 0 | `input.args[0]` | [1, 714, 2880] | torch.bfloat16 → float32 | -41728.0 / 644.0 / 0.45385090091537916 / 35.353335853041926 | [NPY](tensors/0000067.npy) |
| 68 | `model.layers.11.post_attention_layernorm` | 0 | `output` | [1, 714, 2880] | torch.bfloat16 → float32 | -78.5 / 7.8125 / 0.009589803441135756 / 0.7561778205261509 | [NPY](tensors/0000068.npy) |
| 69 | `model.layers.11.mlp` | 0 | `input.args[0]` | [1, 714, 2880] | torch.bfloat16 → float32 | -78.5 / 7.8125 / 0.009589803441135756 / 0.7561778205261509 | [NPY](tensors/0000069.npy) |
| 70 | `model.layers.11.mlp.experts` | 0 | `input.args[0]` | [714, 2880] | torch.bfloat16 → float32 | -78.5 / 7.8125 / 0.009589803441135756 / 0.7561778205261509 | [NPY](tensors/0000070.npy) |
| 71 | `model.layers.11.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 72 | `model.layers.11.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 73 | `model.layers.11.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 74 | `model.layers.11.mlp.experts` | 0 | `output` | [714, 2880] | torch.bfloat16 → float32 | -430.0 / 388.0 / 0.09105190028315611 / 7.891203985929962 | [NPY](tensors/0000074.npy) |
| 75 | `model.layers.11.mlp` | 0 | `output[0]` | [1, 714, 2880] | torch.bfloat16 → float32 | -430.0 / 388.0 / 0.09105190028315611 / 7.891203985929962 | [NPY](tensors/0000075.npy) |
| 76 | `model.layers.11.mlp` | 0 | `output[1]` | [714, 32] | torch.bfloat16 → float32 | -10.75 / 3.625 / -0.15380987833861878 / 0.7362932545068505 | [NPY](tensors/0000076.npy) |
| 77 | `model.layers.11` | 0 | `output` | [1, 714, 2880] | torch.bfloat16 → float32 | -41728.0 / 848.0 / 0.5449083301533504 / 38.130638129314455 | [NPY](tensors/0000077.npy) |

## Layer 0023

| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 78 | `model.layers.23` | 0 | `input.args[0]` | [1, 714, 2880] | torch.bfloat16 → float32 | -12672.0 / 14208.0 / -1.0551274182972339 / 411.9628090297926 | [NPY](tensors/0000078.npy) |
| 79 | `model.layers.23` | 0 | `input.kwargs['attention_mask']` | [1, 1, 714, 714] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6923920732047232e+38 / 1.6947640324250779e+38 | [NPY](tensors/0000079.npy) |
| 80 | `model.layers.23` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 714, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7411219109037593 / 0.9062333078556434 | [NPY](tensors/0000080.npy) |
| 81 | `model.layers.23` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 714, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10502767491443618 / 0.6543104876572913 | [NPY](tensors/0000081.npy) |
| 82 | `model.layers.23` | 0 | `input.kwargs['position_ids']` | [1, 714] | torch.int64 → int64 | 0.0 / 713.0 / 356.5 / 206.11384394714165 | [NPY](tensors/0000082.npy) |
| 83 | `model.layers.23` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 84 | `model.layers.23` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 85 | `model.layers.23` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 86 | `model.layers.23.input_layernorm` | 0 | `input.args[0]` | [1, 714, 2880] | torch.bfloat16 → float32 | -12672.0 / 14208.0 / -1.0551274182972339 / 411.9628090297926 | [NPY](tensors/0000086.npy) |
| 87 | `model.layers.23.input_layernorm` | 0 | `output` | [1, 714, 2880] | torch.bfloat16 → float32 | -57.25 / 70.5 / 0.01001543996039948 / 1.7588262247772206 | [NPY](tensors/0000087.npy) |
| 88 | `model.layers.23.self_attn` | 0 | `input.kwargs['hidden_states']` | [1, 714, 2880] | torch.bfloat16 → float32 | -57.25 / 70.5 / 0.01001543996039948 / 1.7588262247772206 | [NPY](tensors/0000088.npy) |
| 89 | `model.layers.23.self_attn` | 0 | `input.kwargs['attention_mask']` | [1, 1, 714, 714] | torch.bfloat16 → float32 | -3.3895313892515355e+38 / 0.0 / -1.6923920732047232e+38 / 1.6947640324250779e+38 | [NPY](tensors/0000089.npy) |
| 90 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_ids']` | [1, 714] | torch.int64 → int64 | 0.0 / 713.0 / 356.5 / 206.11384394714165 | [NPY](tensors/0000090.npy) |
| 91 | `model.layers.23.self_attn` | 0 | `input.kwargs['past_key_values']` | — | NoneType | None | — |
| 92 | `model.layers.23.self_attn` | 0 | `input.kwargs['use_cache']` | — | bool | False | — |
| 93 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_embeddings'][0]` | [1, 714, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.7411219109037593 / 0.9062333078556434 | [NPY](tensors/0000093.npy) |
| 94 | `model.layers.23.self_attn` | 0 | `input.kwargs['position_embeddings'][1]` | [1, 714, 32] | torch.bfloat16 → float32 | -1.34375 / 1.34375 / 0.10502767491443618 / 0.6543104876572913 | [NPY](tensors/0000094.npy) |
| 95 | `model.layers.23.self_attn` | 0 | `input.kwargs['output_hidden_states']` | — | bool | False | — |
| 96 | `model.layers.23.self_attn.q_proj` | 0 | `input.args[0]` | [1, 714, 2880] | torch.bfloat16 → float32 | -57.25 / 70.5 / 0.01001543996039948 / 1.7588262247772206 | [NPY](tensors/0000096.npy) |
| 97 | `model.layers.23.self_attn.q_proj` | 0 | `output` | [1, 714, 4096] | torch.bfloat16 → float32 | -19.625 / 25.0 / 0.034192582063256205 / 1.6551792290388685 | [NPY](tensors/0000097.npy) |
| 98 | `model.layers.23.self_attn.k_proj` | 0 | `input.args[0]` | [1, 714, 2880] | torch.bfloat16 → float32 | -57.25 / 70.5 / 0.01001543996039948 / 1.7588262247772206 | [NPY](tensors/0000098.npy) |
| 99 | `model.layers.23.self_attn.k_proj` | 0 | `output` | [1, 714, 512] | torch.bfloat16 → float32 | -85.5 / 66.0 / -0.06781504878804286 / 5.08785514966508 | [NPY](tensors/0000099.npy) |
| 100 | `model.layers.23.self_attn.v_proj` | 0 | `input.args[0]` | [1, 714, 2880] | torch.bfloat16 → float32 | -57.25 / 70.5 / 0.01001543996039948 / 1.7588262247772206 | [NPY](tensors/0000100.npy) |
| 101 | `model.layers.23.self_attn.v_proj` | 0 | `output` | [1, 714, 512] | torch.bfloat16 → float32 | -33.25 / 23.375 / -0.0004657855158259547 / 3.368228260550392 | [NPY](tensors/0000101.npy) |
| 102 | `model.layers.23.self_attn.o_proj` | 0 | `input.args[0]` | [1, 714, 4096] | torch.bfloat16 → float32 | -32.25 / 17.5 / -0.0018040882172052457 / 1.2231587523092495 | [NPY](tensors/0000102.npy) |
| 103 | `model.layers.23.self_attn.o_proj` | 0 | `output` | [1, 714, 2880] | torch.bfloat16 → float32 | -6784.0 / 7072.0 / 2.811207868803931 / 161.4673284067516 | [NPY](tensors/0000103.npy) |
| 104 | `model.layers.23.self_attn` | 0 | `output[0]` | [1, 714, 2880] | torch.bfloat16 → float32 | -6784.0 / 7072.0 / 2.811207868803931 / 161.4673284067516 | [NPY](tensors/0000104.npy) |
| 105 | `model.layers.23.self_attn` | 0 | `output[1]` | [1, 64, 714, 714] | torch.bfloat16 → float32 | 0.0 / 1.0 / 0.0007265702228440561 / 0.008562727048660056 | [NPY](tensors/0000105.npy) |
| 106 | `model.layers.23.post_attention_layernorm` | 0 | `input.args[0]` | [1, 714, 2880] | torch.bfloat16 → float32 | -11648.0 / 11392.0 / 1.7561791413749746 / 387.1373933006705 | [NPY](tensors/0000106.npy) |
| 107 | `model.layers.23.post_attention_layernorm` | 0 | `output` | [1, 714, 2880] | torch.bfloat16 → float32 | -50.5 / 23.375 / -0.013103186618565696 / 1.245771616810726 | [NPY](tensors/0000107.npy) |
| 108 | `model.layers.23.mlp` | 0 | `input.args[0]` | [1, 714, 2880] | torch.bfloat16 → float32 | -50.5 / 23.375 / -0.013103186618565696 / 1.245771616810726 | [NPY](tensors/0000108.npy) |
| 109 | `model.layers.23.mlp.experts` | 0 | `input.args[0]` | [714, 2880] | torch.bfloat16 → float32 | -50.5 / 23.375 / -0.013103186618565696 / 1.245771616810726 | [NPY](tensors/0000109.npy) |
| 110 | `model.layers.23.mlp.experts` | 0 | `input.args[1]` | — | RoutingData | opaque object or empty container; no tensor leaf exposed | — |
| 111 | `model.layers.23.mlp.experts` | 0 | `input.args[2]` | — | GatherIndx | opaque object or empty container; no tensor leaf exposed | — |
| 112 | `model.layers.23.mlp.experts` | 0 | `input.kwargs['scatter_idx']` | — | ScatterIndx | opaque object or empty container; no tensor leaf exposed | — |
| 113 | `model.layers.23.mlp.experts` | 0 | `output` | [714, 2880] | torch.bfloat16 → float32 | -6592.0 / 6528.0 / -1.4015935967876054 / 160.89835331226084 | [NPY](tensors/0000113.npy) |
| 114 | `model.layers.23.mlp` | 0 | `output[0]` | [1, 714, 2880] | torch.bfloat16 → float32 | -6592.0 / 6528.0 / -1.4015935967876054 / 160.89835331226084 | [NPY](tensors/0000114.npy) |
| 115 | `model.layers.23.mlp` | 0 | `output[1]` | [714, 32] | torch.bfloat16 → float32 | -8.3125 / 5.0 / 0.21350405730453192 / 2.449283614827986 | [NPY](tensors/0000115.npy) |
| 116 | `model.layers.23` | 0 | `output` | [1, 714, 2880] | torch.bfloat16 → float32 | -11904.0 / 12032.0 / 0.3549783117185676 / 394.19331629955064 | [NPY](tensors/0000116.npy) |

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
