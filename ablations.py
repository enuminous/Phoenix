from benchmark import reference, trajectory, invariants
from phoenix import PhoenixEvaluator

if __name__ == "__main__":
    ev = PhoenixEvaluator(reference)
    full = ev.evaluate_trajectory(trajectory,invariants,threshold=0.9,hold=2)
    no_hold = ev.evaluate_trajectory(trajectory,invariants,threshold=0.9,hold=1)
    print("full stable recovery:", full["stable_recovery"], "time:", full["recovery_time"])
    print("no hold requirement:", no_hold["stable_recovery"], "time:", no_hold["recovery_time"])
