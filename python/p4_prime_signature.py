from __future__ import annotations

from new_foundations.python.core import is_prime
from .util_parity import parity_tensor

ID = "S2.P4.1-PrimeSignature"
NAME = "All odd primes have parity tensor (1,1,0)"
DEPENDS_ON = ("S2.T3.1-ParityClasses",)


def check(limit: int = 200000) -> None:
    for n in range(3, limit + 1, 2):
        if is_prime(n):
            assert parity_tensor(n) == (1, 1, 0), (
                f"Odd prime {n} has wrong tensor {parity_tensor(n)}"
            )

