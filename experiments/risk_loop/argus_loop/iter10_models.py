"""Iteration 10 model T10-1 (train only). Plan: reports/risk-loop/argus-v1/loop/iter-10/plan.md.

T10-1: ensemble MEMBER SELECTION inside nested CV. The grid is the 15 non-empty subsets of four fixed members
(all on the robust embedding store of iteration 7, fixed hyperparameters):
  0 H2-1c-L23 pointwise (L23 max, k 32, C 0.1)      1 T4-1a pair (L23 max, k 32, C 0.001)
  2 T4-1b pair (L16 pre, k 10, C 0.01)               3 T6-1 same-trajectory+same-tool pair (L23 max, k 10, C 0.1)
The frozen v4 ``evaluate.nested_cv`` inner CV (inner v3 headline) picks one subset per outer fold; the subset
is scored as the equal-weight average of its members' training-score percentiles (as iterations 6-9).

Member scores are memoised per (member, pos_train, y_train, pos_test) in a bounded LRU so the 15 subsets reuse
the 4 member fits of every inner fold; labels are part of the key, so shuffled-label refits are separate entries.
Scoring reads only the scored rows' embeddings; tool / trajectory / source are read at training rows only.
Earlier files are not modified.
"""
from __future__ import annotations

import hashlib
import itertools
import sys
import threading
from collections import OrderedDict
from pathlib import Path

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))
from experiments.risk_loop.argus_loop import iter06_models as M6  # noqa: E402
from experiments.risk_loop.argus_loop import iter09_models as M9  # noqa: E402

MEMBERS = tuple(M6.ENSEMBLE) + (M9.T61,)   # H2-1c-L23, T4-1a, T4-1b, T6-1
MEMBER_NAMES = tuple(m["name"] for m in MEMBERS)
# Pre-fixed order: by subset size, then member index (ties in the inner criterion -> first entry).
GRID = [{"members": list(c)} for r in range(1, len(MEMBERS) + 1)
        for c in itertools.combinations(range(len(MEMBERS)), r)]


def subset_label(g) -> str:
    return "+".join(MEMBER_NAMES[i] for i in g["members"])


def _h(a) -> str:
    a = np.ascontiguousarray(np.asarray(a, dtype=np.int64))
    return hashlib.sha1(a.tobytes()).hexdigest()


class MemberCache:
    """Bounded LRU of member (train-score, test-score) pairs; thread-safe (shuffles run in threads)."""

    def __init__(self, store, ctx: dict, members=MEMBERS, maxsize: int = 96, enabled: bool = True):
        self.store, self.ctx, self.members = store, ctx, members
        self.maxsize, self.enabled = maxsize, enabled
        self.d = OrderedDict()
        self.lock = threading.Lock()
        self.hits = self.misses = 0

    def scores(self, i: int, pos_train, y_train, pos_test):
        key = (i, _h(pos_train), _h(y_train), _h(pos_test))
        if self.enabled:
            with self.lock:
                if key in self.d:
                    self.d.move_to_end(key)
                    self.hits += 1
                    return self.d[key]
        out = M6._component_scores(self.members[i], self.store, self.ctx, pos_train, y_train, pos_test)
        if self.enabled:
            with self.lock:
                self.misses += 1
                self.d[key] = out
                while len(self.d) > self.maxsize:
                    self.d.popitem(last=False)
        return out

    def clear(self):
        with self.lock:
            self.d.clear()


def make_subset(cache: MemberCache):
    """make_fit_predict(g) for T10-1; g = {"members": [member indices]} (equal weights)."""
    def make(g):
        idx = [int(i) for i in g["members"]]
        if not idx:
            raise ValueError("empty subset")

        def fp(pos_train, y_train, pos_test):
            pos_train = np.asarray(pos_train, dtype=np.int64)
            pos_test = np.asarray(pos_test, dtype=np.int64)
            y_train = np.asarray(y_train).astype(np.int64)
            acc = np.zeros(len(pos_test))
            for i in idx:
                s_tr, s_te = cache.scores(i, pos_train, y_train, pos_test)
                acc += M6.train_percentile(s_tr, s_te)
            return acc / len(idx)
        return fp
    return make
