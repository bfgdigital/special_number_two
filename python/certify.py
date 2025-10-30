from __future__ import annotations

"""
Certification runner for special_number_two/python parity tensor proofs.

Run from repo root:
  python -m special_number_two.python.certify
"""

import importlib
import sys
from dataclasses import dataclass
from typing import Callable, Dict, List, Tuple


@dataclass
class Proof:
    id: str
    name: str
    deps: Tuple[str, ...]
    fn: Callable[[], None]


PROOF_MODULES = [
    # Section 2
    "t2_fundamental_parity_theorem",
    "c2_p_parity_corollary",
    # Section 3
    "t3_parity_classes",
    # Section 4
    "p4_prime_signature",
    "p4_powers_of_two",
    "p4_semiprimes_and_squares",
    # Section 5
    "t5_multiplicative_relations_mod2",
]


def load_proofs() -> Dict[str, Proof]:
    proofs: Dict[str, Proof] = {}
    pkg = __package__ or "special_number_two.python"
    for mod_name in PROOF_MODULES:
        module = importlib.import_module(f"{pkg}.{mod_name}")
        p = Proof(
            id=getattr(module, "ID"),
            name=getattr(module, "NAME"),
            deps=tuple(getattr(module, "DEPENDS_ON", ())),
            fn=getattr(module, "check"),
        )
        if p.id in proofs:
            raise RuntimeError(f"Duplicate theorem ID: {p.id}")
        proofs[p.id] = p
    return proofs


def topo_sort(nodes: Dict[str, Proof]) -> List[Proof]:
    in_deg: Dict[str, int] = {k: 0 for k in nodes}
    adj: Dict[str, List[str]] = {k: [] for k in nodes}
    for k, proof in nodes.items():
        for dep in proof.deps:
            if dep not in nodes:
                continue
            in_deg[k] += 1
            adj[dep].append(k)
    queue = [k for k, d in in_deg.items() if d == 0]
    order: List[str] = []
    while queue:
        v = queue.pop()
        order.append(v)
        for w in adj.get(v, []):
            in_deg[w] -= 1
            if in_deg[w] == 0:
                queue.append(w)
    if len(order) != len(nodes):
        missing = set(nodes) - set(order)
        raise RuntimeError(f"Cycle detected or missing nodes: {missing}")
    return [nodes[k] for k in order]


def main(argv: List[str] | None = None) -> int:
    proofs = load_proofs()
    ordered = topo_sort(proofs)
    print("Certifying special_number_two (Parity Tensor)\n")
    failures = 0
    for i, p in enumerate(ordered, start=1):
        dep_str = ", ".join(p.deps) if p.deps else "—"
        print(f"[{i:02d}/{len(ordered)}] {p.id} :: {p.name}")
        print(f"      deps: {dep_str}")
        try:
            p.fn()  # default bounds
            print("      status: OK\n")
        except AssertionError as e:
            failures += 1
            print(f"      status: FAIL — {e}\n")
        except Exception as e:
            failures += 1
            print(f"      status: ERROR — {e}\n")
    print("Summary: {} passed, {} failed".format(len(ordered) - failures, failures))
    return 1 if failures else 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main(sys.argv[1:]))

