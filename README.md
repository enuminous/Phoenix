# PHOENIX — EFMW Zoo #39

**Post-Hazard Operational Evaluation, Network Integrity and eXperimental Recovery**

PHOENIX is an experimental EFMW-inspired framework for evaluating how well a system recovers after severe degradation, partial collapse, or near-catastrophic failure.

## Core question

> Did the system actually recover, or did it merely resume operation in a damaged state?

PHOENIX distinguishes restart from restoration.

## Primary outputs

- recovery completeness
- residual damage
- integrity restoration
- recovery time
- recurrence risk
- reconstruction fidelity
- dependency restoration
- post-recovery drift

## Repository contents

- `theory.md`
- `architecture.md`
- `recovery_model.md`
- `limitations.md`
- `phoenix.py`
- `benchmark.py`
- `ablations.py`
- `test_phoenix.py`
- `example.py`
- `paper.md`
- `CITATION.cff`
- `LICENSE`

## Quick start

```bash
python example.py
python benchmark.py
python ablations.py
python -m unittest test_phoenix.py
```

## Zoo position

TERMITE #38 studies collective emergence.

**PHOENIX #39 asks whether a damaged system can reconstruct operational integrity after the failure has already happened.**
