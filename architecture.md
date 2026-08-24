# PHOENIX Architecture

## Pipeline

1. Healthy-State Snapshotter
2. Hazard Event Recorder
3. Recovery Checkpoint Collector
4. State Fidelity Evaluator
5. Invariant Validator
6. Capability Restoration Analyzer
7. Dependency Integrity Scanner
8. Recurrence Risk Estimator
9. Recovery Stability Monitor
10. Audit Reporter

## Inputs

- pre-hazard reference state
- hazard timestamp
- recovery checkpoints
- invariants
- critical capability tests
- dependency states

## Outputs

```json
{
  "recovery_completeness": 0.91,
  "reconstruction_fidelity": 0.94,
  "integrity_restoration": 1.0,
  "capability_restoration": 0.89,
  "residual_damage": 0.09,
  "stable_recovery": true
}
```

## Design principle

PHOENIX should not define recovery as "service responds."

Recovery requires sufficient restoration of the state that made the system trustworthy before the hazard.

## Integration

JELLYFISH can identify damaged dependencies.

BEAVER can evaluate recovery repairs.

WOLF can detect precursor recurrence.

ELEPHANT can preserve incident and recovery history.
