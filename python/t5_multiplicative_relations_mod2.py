from __future__ import annotations

from new_foundations.python.core import A, M, P

ID = "S2.T5.1-MultiplicativeRelationsMod2"
NAME = "M(mn)≡M(m)M(n), A(mn)≡A(m)+A(n), and P from M,A (mod 2)"
DEPENDS_ON = ("S2.T2.1-FundamentalParity",)


def check(bound: int = 5000) -> None:
    for m in range(2, bound + 1):
        for n in range(2, min(bound // m, bound) + 1):
            # M multiplicative mod 2
            assert (M(m * n) & 1) == ((M(m) & 1) * (M(n) & 1)), (
                f"M multiplicativity mod2 failed at {m},{n}"
            )
            # A additive mod 2
            assert (A(m * n) & 1) == ((A(m) + A(n)) & 1), (
                f"A additivity mod2 failed at {m},{n}"
            )
            # P from M and A
            lhs = P(m * n) & 1
            rhs = ((M(m * n) - A(m * n)) & 1)
            rhs2 = ((M(m) & 1) * (M(n) & 1) + (A(m) & 1) + (A(n) & 1)) & 1
            assert lhs == rhs == rhs2, f"P parity failed at {m},{n}"

