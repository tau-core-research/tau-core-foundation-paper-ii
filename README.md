# Tau Core Foundation Paper II

## Finite Source Signatures, Joint Incidence, and Representation Uniqueness

This repository contains the second manuscript in the foundation sequence and
the reproducibility package for the finite joint-source results extracted from
Foundation Paper I.  It identifies the source information required before the
record-transport problem treated in Foundation Paper III is meaningful.

The paper covers:

- complete finite typed source signatures;
- GNS uniqueness of minimal cyclic realizations;
- bipartite marginal non-identifiability;
- the general \(n\)-qudit all-proper-marginal no-go;
- the exact `174 + 81 = 255` Pauli-direction audit;
- descriptor-rank and noise-stability tests;
- one onto joint-incidence sufficient theorem and singular-value bounds;
- precise separation of representation selection by `Pi_phys` from state
  occupation by the incidence/stiffness packet;
- countermodels, a complete worked `M_2(C)` packet, a conditioning figure and
  a reproducible finite verification certificate.

## Claim Boundary

The paper does not prove that the physical Tau parent creates or occupies the
required joint incidence or `Pi_phys`. It contains finite representation and
non-identifiability theorems, not empirical validation or terminal physics.

## Reproduce

```bash
python3 scripts/reproduce.py
```

Outputs:

- `paperII_submission_source/main.pdf`
- `arxiv_submission_source.zip`

The current manuscript is 16 A4 pages and the public package tests pass 5/5.
Its opening series map and notation ledger use the same dependency direction
and symbols as Foundation Papers I and III.
