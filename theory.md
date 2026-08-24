# PHOENIX Theory

## 1. Problem

A system can appear recovered because:
- processes restarted,
- traffic resumed,
- error rate fell,
- services answered again.

Yet deeper damage may remain:
- corrupted state,
- missing dependencies,
- weakened redundancy,
- latent inconsistency,
- elevated recurrence risk,
- degraded performance.

PHOENIX evaluates recovery as a multi-dimensional restoration process.

## 2. Pre-hazard reference

Let the last known healthy state be:

`x_ref`

Hazard produces degraded state:

`x_fail`

Recovery produces:

`x_rec(t)`

## 3. Reconstruction fidelity

For normalized state distance:

`D_t = dist(x_rec(t), x_ref)`

Recovery fidelity:

`F_t = 1 - D_t`

Higher is better.

## 4. Integrity restoration

Let required invariants be:

`I = {I_1, ..., I_k}`

Integrity score:

`G_t = passed_invariants / total_invariants`

## 5. Functional restoration

Let required capabilities be weighted by criticality.

`Q_t = sum_j w_j * capability_j(t)`

## 6. Residual damage

Residual damage may include:
- state divergence,
- failed dependencies,
- reduced redundancy,
- degraded capacity,
- unresolved corruption.

Candidate score:

`R_t = 1 - (alpha*F_t + beta*G_t + gamma*Q_t)`

## 7. Recovery time

If hazard occurs at `T_h` and healthy criteria are again met at `T_r`:

`T_recovery = T_r - T_h`

## 8. Recurrence risk

A fast restart may return the system to the same unstable basin.

Let precursor burden after recovery be `P_post`.

Candidate recurrence risk:

`K = f(P_post, unresolved_root_cause, residual_damage)`

## 9. Recovery trajectory

PHOENIX tracks:

`x_fail -> x_partial -> x_restored`

rather than only measuring the endpoint.

This allows detection of unstable or oscillatory recovery.

## 10. EFMW interpretation

The EFMW-inspired element is recursive restoration across state, relationships, invariants, and dependencies.

The central distinction is:

**operational again** versus **structurally recovered**.

## 11. Falsifiable prediction

PHOENIX should add value when:
- restart is easier than true restoration,
- state consistency matters,
- dependencies recover asynchronously,
- recurrence risk persists after apparent recovery.

If ordinary uptime and incident metrics capture equivalent recovery quality, PHOENIX is unnecessary.
