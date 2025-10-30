from __future__ import annotations

from typing import Dict, Tuple

from .util_parity import parity_tensor

ID = "S2.T3.1-ParityClasses"
NAME = "Only four parity tensors occur, per M ≡ A+P (mod 2)"
DEPENDS_ON = ("S2.T2.1-FundamentalParity",)


FOUR = {(0, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 0)}


def check(limit: int = 20000) -> None:
    seen: Dict[Tuple[int, int, int], int] = {}
    for n in range(2, limit + 1):
        t = parity_tensor(n)
        # Enforce constraint M ≡ A+P (mod 2)
        assert t[0] == ((t[1] + t[2]) & 1), f"Constraint M≡A+P failed at n={n}, T={t}"
        assert t in FOUR, f"Unexpected parity tensor at n={n}: T={t}"
        seen[t] = seen.get(t, 0) + 1
    # All four classes should appear by a modest bound
    assert set(seen) == FOUR, f"Not all four classes observed; seen={set(seen)}"

