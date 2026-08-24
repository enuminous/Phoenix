# Limitations and Falsification

PHOENIX is an experimental recovery-evaluation framework.

## Limitations

- A healthy reference state may be unavailable.
- Some systems legitimately recover to a different configuration.
- State distance metrics may be misleading.
- Invariants may be incomplete.
- Recovery can depend on external systems not instrumented.
- Recurrence risk is difficult to estimate.

## Falsification criteria

PHOENIX's central hypothesis is weakened if:

1. Standard incident metrics predict recurrence equally well.
2. Reference-state fidelity adds no value.
3. Invariant restoration does not correlate with reliability.
4. Dependency restoration adds no predictive information.
5. Results fail across held-out incidents.
6. Stable-hold criteria do not improve recovery classification.

## Claim boundary

PHOENIX evaluates recovery under supplied state, invariants, and capability tests. It cannot prove that all latent damage has been removed.
