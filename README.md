# Tau Core Technical Paper I

**Foundation-series position:** Paper II

## Finite Source Signatures, Joint Incidence, and Representation Uniqueness

This repository contains the second manuscript in the foundation sequence and
the reproducibility package for the finite joint-source results extracted from
Foundation Paper I. It identifies the source information required before the
record-transport problem treated in Technical Paper II (series Paper III) is
meaningful.

## Atemporal Parent-Realization Terminology

Because the Tau parent is atemporal, “Nature selects” does not mean an
external agent or a later decision. It is legacy shorthand for the internal
physical implication

\[
(B_\tau^{\mathrm{phys}},s_U,\mathcal L_{\mathrm{parent}})
\Longrightarrow \mathfrak P,
\]

together with physical occupation of the support of \(\mathfrak P\). A theorem
inside a declared completion proves only class-relative realization; it does
not prove this unrestricted base–seed arrow. Agreement of finitely many
terminal readouts also cannot establish ambient-source exhaustivity. The
current terminology is therefore **parent-law realization** and **physical
occupation**.

## Observer Co-Descent

This paper inherits Paper I's convention: `O` is a body-side carrier candidate
before operational closure. Rank-four descent, stable quantization and a
nonzero record/effect co-produce the observer and its accessible 4D world.
The finite source signature supports this closure but is not observerhood by
itself.


The paper covers:

- complete finite typed source signatures;
- GNS uniqueness of minimal cyclic realizations;
- bipartite marginal non-identifiability;
- the general \(n\)-qudit all-proper-marginal no-go;
- the exact `174 + 81 = 255` Pauli-direction audit;
- descriptor-rank and noise-stability tests;
- one onto joint-incidence sufficient theorem and singular-value bounds;
- the cyclic generated-support theorem and its local quadratic block-reachability
  criterion;
- precise separation of representation selection by `Pi_phys` from state
  occupation by the incidence/stiffness packet;
- the source-signature requirement that one common observer-access map precede
  typed primitive terminal and resolution maps, with stacked rank bounded by
  that common access;
- countermodels, a complete worked `M_2(C)` packet, a conditioning figure and
  a reproducible finite verification certificate.

## Claim Boundary

An exact Schur criterion now closes finite-local support: positive unloaded
split irreps have zero occupation, while stable loaded or cross-coupled irreps
belong to generated support. Ambient representation exhaustivity remains open.

Faithful finite occupation in this paper is distinct from global
cross-terminal faithfulness. The latter is the injectivity needed to lift
operational subsystem composition back to an exact parent valuation.

The paper does not prove that the physical Tau parent creates or occupies the
required joint incidence or `Pi_phys`. It contains finite representation and
non-identifiability theorems, not empirical validation or terminal physics.

A later hub backport now records that one enriched primary packet conditionally
constructs the joint algebra, faithful state, onto incidence and representation
target used here. Cyclic generated support reaches every typed block, and
stable record existence selects complete occupation inside the declared
source-irredundant MVP carrier class. This closes internal realizability and
class-relative occupation, not unrestricted parent-law realization and
occupation: an
inequivalent energy-sharing or rank-novel completion is not excluded by the
current narrow reduct.

## Reproduce

```bash
python3 scripts/reproduce.py
```

Outputs:

- `paperII_submission_source/main.pdf`
- `arxiv_submission_source.zip`

The current manuscript is 18 A4 pages and the public package tests pass 5/5.
Its opening series map and notation ledger use the same dependency direction
and symbols as Foundation Papers I and III.
