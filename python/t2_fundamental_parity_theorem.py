from __future__ import annotations

from .util_parity import omega_odd
from new_foundations.python.core import A

ID = "S2.T2.1-FundamentalParity"
NAME = "A(n) ≡ ω_odd(n) (mod 2)"
DEPENDS_ON = ()


def check(limit: int = 20000) -> None:
    # Verify parity match up to limit
    for n in range(2, limit + 1):
        assert (A(n) & 1) == (omega_odd(n) & 1), (
            f"Parity mismatch at n={n}: A(n)%2={A(n)&1}, ω_odd%2={omega_odd(n)&1}"
        )

