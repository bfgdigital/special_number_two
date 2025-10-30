from __future__ import annotations

from .util_parity import omega_odd
from new_foundations.python.core import A, P

ID = "S2.C2.2-PParity"
NAME = "P(n) ≡ n + ω_odd(n) (mod 2) and P ≡ n + A (mod 2)"
DEPENDS_ON = ("S2.T2.1-FundamentalParity",)


def check(limit: int = 50000) -> None:
    for n in range(2, limit + 1):
        lhs = P(n) & 1
        rhs1 = (n + A(n)) & 1
        rhs2 = (n + omega_odd(n)) & 1
        assert lhs == rhs1 == rhs2, (
            f"P-parity mismatch at n={n}: P%2={lhs}, n+A%2={rhs1}, n+ω%2={rhs2}"
        )

