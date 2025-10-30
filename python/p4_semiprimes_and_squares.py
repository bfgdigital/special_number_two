from __future__ import annotations

from new_foundations.python.core import primes_up_to
from .util_parity import parity_tensor

ID = "S2.P4.3-SemiprimesAndSquares"
NAME = "Odd semiprimes and odd prime squares have tensor (1,0,1)"
DEPENDS_ON = ("S2.T3.1-ParityClasses",)


def check(limit_prime: int = 97) -> None:
    ps = [p for p in primes_up_to(limit_prime) if p % 2 == 1]
    # Odd prime squares
    for p in ps:
        n = p * p
        assert parity_tensor(n) == (1, 0, 1), (
            f"Odd square {p}^2 tensor {parity_tensor(n)} != (1,0,1)"
        )
    # Distinct odd semiprimes
    for i, p in enumerate(ps):
        for q in ps[i + 1 :]:
            n = p * q
            assert parity_tensor(n) == (1, 0, 1), (
                f"Odd semiprime {p}*{q} tensor {parity_tensor(n)} != (1,0,1)"
            )

