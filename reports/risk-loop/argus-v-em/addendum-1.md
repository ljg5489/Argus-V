# Argus-V-em round 01 addendum 1 — same-target linear control

Fixed 2026-11-15 before running this control. The first learned-embedding round already produced its OOF scores; this addendum prevents attributing the gain to the embedding without a like-for-like control.

- Model: raw concatenated hidden state → one linear score; no projection bottleneck, GELU, or dropout.
- Keep the round 01 training labels, negative sampling rule, robust scaling, 5 family-grouped folds × seeds 0/1/2, 60 epochs, AdamW, loss and per-fold seeds unchanged.
- Report the same visible-positive metric and the same all-violation context. Do not use the result to change the already reported round 01 score.
- If the linear control also reaches 0.90, treat the target score as evidence for the target labels/features, not evidence that a learned embedding helped.
