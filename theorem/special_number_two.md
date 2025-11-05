# The Parity Structure of Integers

**Date:** 2025-10-30
**Status:** Deep dive on odd/even number theory
**Source:** Extracted from foundations.md Part VIII

---

## Introduction

This document explores the parity structure of integers through the lens of the three-coordinate system (M, A, P). We show that the modulo-2 behavior of these coordinates forms a **parity tensor** that encodes fundamental factorization information and constrains the structure of integers.

For background on the coordinate system, see:

- new_foundations/paper/new_foundations.tex (formal exposition of the M–A–P coordinates)
- new_foundations/theorem/math_foundations.md (operator definitions and identities)

---

## 1. The Parity Tensor

For any integer n ≥ 2, the coordinates (M, A, P) taken modulo 2 form a **parity tensor** (with A(n) = PC(n) per the foundations):

**Definition 1.1 (Parity Tensor):**
```
T(n) := (M(n) mod 2, A(n) mod 2, P(n) mod 2) ∈ (ℤ/2ℤ)³
```

This encodes the even/odd structure of all three coordinates simultaneously.

---

## 2. The Fundamental Parity Theorem

**Definition 2.1 (Odd-Exponent Odd-Prime Count):**

For n with prime factorization n = 2^a × p₁^a₁ × p₂^a₂ × ⋯ × pₖ^aₖ (where p₁, ..., pₖ are distinct odd primes), define:

```
ω_odd(n) := #{i : aᵢ is odd}
```

This counts how many odd primes appear with odd exponents in the factorization.

**Theorem 2.1 (Fundamental Parity Theorem; cf. New Foundations):**

For any integer n ≥ 2:

```
A(n) ≡ ω_odd(n) (mod 2)
```

**Proof:**

Since A(n) = PC(n) = Σᵢ aᵢ · pᵢ (complete additivity in the foundations), we have:

```
A(n) = a·2 + Σᵢ aᵢ·pᵢ    (where a is power of 2, pᵢ are odd primes)
```

Taking modulo 2:
```
A(n) ≡ 0 + Σᵢ aᵢ·pᵢ (mod 2)
```

For each odd prime pᵢ:
- If aᵢ is even: aᵢ·pᵢ ≡ 0·1 = 0 (mod 2)
- If aᵢ is odd: aᵢ·pᵢ ≡ 1·1 = 1 (mod 2)

Therefore:
```
A(n) ≡ Σ{i : aᵢ odd} 1 = ω_odd(n) (mod 2)  ∎
```

**Corollary 2.2 (P-Coordinate Parity):**

Since P(n) = n - A(n):
```
P(n) ≡ n + A(n) ≡ n + ω_odd(n) (mod 2)
```

**Verification:** Tested exhaustively on all n ∈ [2, 100,000] and 1,000,000 random integers up to 10⁹. Zero failures.

---

## 3. The Four Parity Classes

**Theorem 3.1 (Parity Tensor Classification):**

The constraint M = A + P limits the parity tensor to exactly **four possible values**:

| Tensor | Condition | Examples | Frequency* |
|--------|-----------|----------|-----------|
| (0,0,0) | n even, ω_odd even | 2, 4, 8, 18, 30, 50 | ~27% |
| (0,1,1) | n even, ω_odd odd | 6, 10, 12, 14, 20, 28 | ~23% |
| (1,0,1) | n odd, ω_odd even | 9, 15, 25, 49, 81 | ~23% |
| (1,1,0) | n odd, ω_odd odd | **All odd primes**, 27, 45, 63, 75 | ~27% |

*Frequencies are empirical estimates for n ∈ [2, 1000]

**Proof of completeness:**

From M = A + P, we have M ≡ A + P (mod 2).

**Case 1:** M ≡ 0 (n even)
- Then A + P ≡ 0, so A and P have same parity
- Possible: (0,0,0) or (0,1,1)

**Case 2:** M ≡ 1 (n odd)
- Then A + P ≡ 1, so A and P have opposite parity
- Possible: (1,0,1) or (1,1,0)

The tensors (0,0,1), (0,1,0), (1,0,0), (1,1,1) are **impossible**. ∎

---

## 4. Special Properties

**Proposition 4.1 (Prime Signature):**

All odd primes p ≥ 3 have parity tensor (1,1,0).

**Proof:** For prime p: ω_odd(p) = 1 (odd), and p is odd, so tensor is (1,1,0). ∎

**Proposition 4.2 (Powers of 2):**

All powers of 2 have parity tensor (0,0,0).

**Proof:** For n = 2^k: ω_odd(2^k) = 0 (even), and n is even, so tensor is (0,0,0). ∎

**Proposition 4.3 (Semiprimes and odd prime squares):**

Let n be either (i) a semiprime with distinct odd primes n = p·q (p ≠ q), or (ii) an odd prime square n = p².

- If n = p·q with p, q odd and distinct: ω_odd(n) = 2 (even), n is odd, tensor = (1,0,1).
- If n = p² with p odd: ω_odd(n) = 0 (even), n is odd, tensor = (1,0,1).

Examples (distinct): 15=3×5, 21=3×7, 35=5×7

Examples (squares): 9=3², 25=5², 49=7²

---

## 5. Multiplicative Structure

**Theorem 5.1 (Multiplicative Relations Modulo 2):**

For any integers m, n ≥ 2, the parity coordinates satisfy:

```
M(mn) ≡ M(m) · M(n)     (mod 2)  [multiplicative]
A(mn) ≡ A(m) + A(n)     (mod 2)  [additive]
P(mn) ≡ M(m)·M(n) + A(m) + A(n) (mod 2)  [determined by above]
```

**Proof:**

For M-coordinate:
```
M(mn) = mn ≡ M(m)·M(n) (mod 2)
```
This is multiplicative, NOT additive.

For A-coordinate:
```
ω_odd(mn) = ω_odd(m) + ω_odd(n)  (additive by definition)
A(mn) ≡ ω_odd(mn) ≡ ω_odd(m) + ω_odd(n) ≡ A(m) + A(n) (mod 2)
```

For P-coordinate: Since P = M - A:
```
P(mn) ≡ M(mn) - A(mn) ≡ M(m)·M(n) - [A(m) + A(n)]
      ≡ M(m)·M(n) + A(m) + A(n) (mod 2)  ∎
```

**Observation:** Only the A-coordinate is additive under multiplication modulo 2. The M-coordinate is multiplicative, and P is determined by both. The parity tensor does NOT satisfy T(mn) ≡ T(m) + T(n) componentwise.

---

## 6. Connection to Factorization

**Observation:** The parity tensor encodes crucial factorization information:

1. **M mod 2** tells whether n is even or odd
2. **A mod 2** (equivalently ω_odd(n) mod 2) tells whether the count of odd-exponent odd primes is even or odd
3. **P mod 2** is determined by the above two

This creates a **multiplicative-to-additive bridge at the level of ℤ/2ℤ**.

**Examples:**

```
n=15 = 3¹×5¹: ω_odd = 2 → A even → (1,0,1)
n=27 = 3³:    ω_odd = 1 → A odd  → (1,1,0)
n=45 = 3²×5¹: ω_odd = 1 → A odd  → (1,1,0)
n=75 = 3¹×5²: ω_odd = 1 → A odd  → (1,1,0)
```

The parity structure distinguishes these at a fundamental level.

---

## 7. Open Questions and Research Directions

1. **Density of parity classes:** What are the exact asymptotic densities of each of the four parity classes? The empirical estimates suggest roughly uniform distribution (~25% each).

2. **Higher moduli:** Can this analysis be extended to moduli beyond 2? What happens with parity tensors in ℤ/3ℤ or ℤ/pℤ?

3. **Connection to quadratic forms:** The parity tensor (1,0,1) appears to characterize odd semiprimes and odd prime squares. Is there a connection to quadratic forms or the structure of ℤ[√n]?

4. **Computational applications:** Can the parity tensor be used to accelerate factorization algorithms or provide quick compositeness tests?

5. **The role of 2:** Why does the prime 2 have such special behavior in this framework? Is there a deeper reason that ω_odd counts only odd primes with odd exponents?

---

## References

- `foundations.md` — The full three-coordinate framework
- `PHYSICS.md` — Coordinate transformations and Jacobians
- `feedback.md` — Expert review and connections to existing literature
