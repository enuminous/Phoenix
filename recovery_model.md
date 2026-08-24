# Recovery Model

## Reference state schema

```json
{
  "capacity": 1.0,
  "consistency": 1.0,
  "redundancy": 1.0,
  "dependency_health": 1.0
}
```

## Recovery state

Each recovery checkpoint records:
- state vector
- invariant results
- capability restoration
- unresolved damage
- time since hazard

## Recovery completeness

A candidate composite:

`C = w1*fidelity + w2*integrity + w3*capability`

## Residual damage

`Damage = 1 - C`

## Stable recovery

A recovery should remain above threshold for a hold period.

This avoids declaring success on a temporary rebound.

## Recurrence risk

Optional features:
- unresolved root cause
- remaining precursor signals
- degraded redundancy
- incomplete dependency restoration
