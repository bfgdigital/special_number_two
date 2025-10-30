from __future__ import annotations

from .util_parity import parity_tensor

ID = "S2.P4.2-PowersOfTwo"
NAME = "All powers of 2 have parity tensor (0,0,0)"
DEPENDS_ON = ("S2.T3.1-ParityClasses",)


def check(max_k: int = 30) -> None:
    for k in range(1, max_k + 1):
        n = 1 << k
        assert parity_tensor(n) == (0, 0, 0), (
            f"2^{k} has wrong tensor {parity_tensor(n)}"
        )

