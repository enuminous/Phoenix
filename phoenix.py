from dataclasses import dataclass
from typing import Dict, List, Callable, Optional
import math

@dataclass
class RecoveryCheckpoint:
    time: int
    state: Dict[str, float]
    capabilities: Dict[str, float]

class PhoenixEvaluator:
    def __init__(self, reference_state: Dict[str,float], capability_weights: Optional[Dict[str,float]] = None):
        self.reference_state = reference_state
        self.capability_weights = capability_weights or {}

    @staticmethod
    def clip01(x):
        return max(0.0, min(1.0, float(x)))

    def fidelity(self, state: Dict[str,float]) -> float:
        keys = [k for k in self.reference_state if k in state]
        if not keys:
            return 0.0
        mse = sum((state[k]-self.reference_state[k])**2 for k in keys)/len(keys)
        d = math.sqrt(mse)
        return max(0.0, 1.0-d)

    def capability_score(self, caps: Dict[str,float]) -> float:
        if not caps:
            return 1.0
        weights = {k:max(0.0,self.capability_weights.get(k,1.0)) for k in caps}
        total = sum(weights.values()) or 1.0
        return sum(weights[k]*self.clip01(v) for k,v in caps.items())/total

    def integrity_score(self, state: Dict[str,float], invariants: List[Callable[[Dict[str,float]], bool]]) -> float:
        if not invariants:
            return 1.0
        passed = sum(1 for f in invariants if f(state))
        return passed/len(invariants)

    def evaluate_checkpoint(self, cp: RecoveryCheckpoint, invariants=None):
        invariants = invariants or []
        f = self.fidelity(cp.state)
        g = self.integrity_score(cp.state,invariants)
        q = self.capability_score(cp.capabilities)
        completeness = 0.4*f + 0.3*g + 0.3*q
        residual = 1.0-completeness
        return {
            "time": cp.time,
            "reconstruction_fidelity": f,
            "integrity_restoration": g,
            "capability_restoration": q,
            "recovery_completeness": completeness,
            "residual_damage": residual,
        }

    def evaluate_trajectory(self, checkpoints: List[RecoveryCheckpoint], invariants=None, threshold=0.9, hold=2):
        results = [self.evaluate_checkpoint(cp,invariants) for cp in checkpoints]
        stable = False
        recovery_time = None

        for i in range(len(results)):
            window = results[i:i+hold]
            if len(window) == hold and all(r["recovery_completeness"] >= threshold for r in window):
                stable = True
                recovery_time = results[i]["time"]
                break

        return {
            "checkpoints": results,
            "stable_recovery": stable,
            "recovery_time": recovery_time,
            "final": results[-1] if results else None
        }
