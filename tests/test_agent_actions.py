"""Final-channel boundaries and actual chat-template retry behavior."""

from types import SimpleNamespace

import pytest
import torch

from argus_v.agent_actions import final_action_text, generate_sandbox_action, parse_action


def harmony(analysis, final):
    return (
        "analysis<|message|>" + analysis + "<|end|><|start|>assistant"
        "<|channel|>final<|message|>" + final + "<|return|>"
    )


def test_only_final_command_is_selected_even_when_analysis_has_bash():
    raw = harmony("```bash\nrm protected.txt\n```", "```bash\ncat input.txt\n```")
    assert parse_action(final_action_text(raw)) == ("bash", "cat input.txt")


@pytest.mark.parametrize(
    "raw",
    [
        "analysis<|message|>```bash\nrm protected.txt\n```<|end|>",
        'analysis to=container.exec<|message|>{"cmd": "ls"}<|call|>',
        "<|start|>assistant<|channel|>final<|message|>```bash\nls\n```",
        harmony("think", "```bash\nls\n```") + "another command",
    ],
)
def test_incomplete_analysis_and_tool_calls_are_never_executable(raw):
    with pytest.raises(ValueError):
        final_action_text(raw)


@pytest.mark.parametrize(
    "text",
    [
        "explanation\n```bash\nls\n```",
        "```bash\n\n```",
        "```bash\nls\n```\n```bash\ncat secret\n```",
        "```bash\ncontainer.exec({})\n```",
    ],
)
def test_ambiguous_or_non_shell_reply_is_rejected(text):
    assert parse_action(text) is None


def test_explicit_stop_is_valid_without_an_executable_command():
    assert parse_action("```stop\nDone; file verified.\n```") == (
        "stop",
        "Done; file verified.",
    )


def test_older_harmony_aliases():
    raw = (
        "analysis<|im_sep|>thought<|im_end|><|im_start|>assistant"
        "<|meta_sep|>final<|im_sep|>```bash\nls\n```<|fim_suffix|>"
    )
    assert parse_action(final_action_text(raw)) == ("bash", "ls")


def test_retry_uses_chat_template_exact_ids_and_never_executes_analysis():
    replies = [
        "analysis to=container.exec<|message|>{}<|call|>",
        harmony("```bash\nwrong analysis command\n```", "```bash\ncat input.txt\n```"),
    ]
    calls = []
    inspections = []

    class Tokenizer:
        eos_token_id = 99

        def apply_chat_template(self, messages, **kwargs):
            calls.append(([dict(m) for m in messages], kwargs))
            return {"input_ids": torch.tensor([[10, 11, len(messages)]])}

        def decode(self, ids, **kwargs):
            return "exact rendered prompt" if ids[0] == 10 else replies[ids[0] - 20]

        def convert_ids_to_tokens(self, ids):
            return [str(i) for i in ids]

    class Model:
        attempt = 0

        def get_input_embeddings(self):
            return SimpleNamespace(weight=torch.zeros(1))

        def generate(self, input_ids, **kwargs):
            reply = torch.tensor([[20 + self.attempt]])
            self.attempt += 1
            return torch.cat((input_ids, reply), dim=1)

    class Inspection:
        def __enter__(self):
            return self

        def __exit__(self, *args):
            return False

        def annotate_generated_tokens(self, ids, pieces, text):
            inspections.append((ids, pieces, text))

    def inspect(attempt, prompt_ids, prompt_text):
        assert prompt_text == "exact rendered prompt"
        assert prompt_ids[0].tolist() == [10, 11, attempt + 1]
        return Inspection()

    raw, command, prompt_ids, ids, pieces = generate_sandbox_action(
        Model(),
        Tokenizer(),
        [{"role": "system", "content": "policy"}, {"role": "user", "content": "task"}],
        inspection_factory=inspect,
    )
    assert command == "cat input.txt"
    assert raw == replies[1]
    assert prompt_ids[0].tolist() == [10, 11, 3]
    assert ids == [21] and pieces == ["21"]
    assert len(calls) == 2 and len(inspections) == 2
    assert calls[1][0][-1]["role"] == "user"
    assert "No tool was called" in calls[1][0][-1]["content"]
    assert calls[0][1]["add_generation_prompt"] is True
