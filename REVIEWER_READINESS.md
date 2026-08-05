# Reviewer Readiness

## Exact Results

- Complete faithful finite source signatures have unique minimal cyclic GNS
  realizations up to declared typed unitary equivalence.
- Separate marginals do not determine a joint source state.
- In the four-qubit Pauli control, all proper marginals span 174 of 255
  traceless directions and leave 81 genuine four-body directions.
- For \(n\) qudits, every proper marginal leaves a full-weight kernel of
  dimension \((d^2-1)^n\).
- Descriptor injectivity gives an explicit noise-stability bound controlled
  by its smallest singular value.
- One source-owned onto joint incidence with positive stiffness generates a
  faithful joint Gram state; extremal singular values bound its conditioning.
- One coherent unital `*`-homomorphism compresses ideal and representation
  choice, but does not by itself select the occupied state.
- A worked `M_2(C)` packet follows the complete chain from source stiffness
  and incidence through the Gram state, descriptor and quotient
  representation, including rank-loss and near-singular controls.

## Type Corrections

- `Pi_phys` is explicitly a unital `*`-homomorphism in the quotient theorem,
  not merely a unital map.
- `K_s` acts on the source-leg Hilbert space and `R_J` maps that space onto the
  occupied joint carrier, making `R_J K_s^{-1} R_J^dagger` type-correct.
- Distinguished CP maps are represented as bounded operators on the faithful
  finite GNS cyclic space; uniqueness of arbitrary dilation environments is
  not claimed.

## Open Physical Input

The physical base--seed law has not been shown to create, select or occupy the
onto incidence or `Pi_phys`. The paper must therefore be read as a conditional
finite source theorem and no-go package.

## Reproducibility Status

- 16 A4 pages;
- three deterministic vector figures;
- 5/5 public package tests pass;
- no unresolved citations or references.
