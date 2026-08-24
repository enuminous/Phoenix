# PHOENIX: Post-Hazard Operational Evaluation, Network Integrity and eXperimental Recovery

## Abstract

PHOENIX is an experimental framework for evaluating post-hazard recovery in complex systems. It distinguishes simple service resumption from restoration of state fidelity, invariants, capabilities, dependencies, and stable operating conditions.

## 1. Motivation

Restarting is not the same as recovering.

A system may resume service while retaining:
- corrupted state,
- reduced redundancy,
- degraded dependencies,
- unstable dynamics.

PHOENIX evaluates recovery quality rather than uptime alone.

## 2. Model

Reference state:

`x_ref`

Recovered state:

`x_rec(t)`

Fidelity:

`F=1-dist(x_rec,x_ref)`

Integrity:

`G=passed_invariants/total_invariants`

Capability restoration:

`Q=weighted capability score`

Composite completeness:

`C=w1*F+w2*G+w3*Q`

Residual damage:

`R=1-C`

## 3. Metrics

- recovery completeness
- residual damage
- reconstruction fidelity
- integrity restoration
- capability restoration
- recovery time
- stability hold
- recurrence risk

## 4. Baselines

- uptime restoration
- mean time to recovery
- incident closure
- service health checks
- simple functional smoke tests

## 5. Ablations

- no healthy reference
- no invariant checks
- no capability weighting
- no stable-hold requirement
- endpoint-only evaluation
- no dependency restoration

## 6. Falsification

If conventional recovery metrics predict recurrence and post-incident reliability equally well, PHOENIX's additional structure is not justified.

## 7. Claim boundary

PHOENIX evaluates only observable and instrumented recovery dimensions. It cannot prove all hidden damage has been removed.
