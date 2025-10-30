from __future__ import annotations

from typing import Tuple

from new_foundations.python.core import A, M, P, factorint


def omega_odd(n: int) -> int:
    """Count odd primes with odd exponents in n's factorization."""
    fac = factorint(n)
    total = 0
    for p, e in fac.items():
        if p % 2 == 1 and (e % 2 == 1):
            total += 1
    return total


def parity_tensor(n: int) -> Tuple[int, int, int]:
    """Return (M mod 2, A mod 2, P mod 2)."""
    return (M(n) & 1, A(n) & 1, P(n) & 1)

