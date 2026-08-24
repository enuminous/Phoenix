from phoenix import PhoenixEvaluator, RecoveryCheckpoint

reference = {
    "capacity":1.0,
    "consistency":1.0,
    "redundancy":1.0,
    "dependency_health":1.0
}

invariants = [
    lambda s: s["consistency"] >= 0.95,
    lambda s: s["redundancy"] >= 0.85,
    lambda s: s["dependency_health"] >= 0.90
]

trajectory = [
    RecoveryCheckpoint(1,{"capacity":0.45,"consistency":0.55,"redundancy":0.35,"dependency_health":0.40},{"serve":0.5,"write":0.2}),
    RecoveryCheckpoint(2,{"capacity":0.70,"consistency":0.75,"redundancy":0.55,"dependency_health":0.70},{"serve":0.75,"write":0.55}),
    RecoveryCheckpoint(3,{"capacity":0.88,"consistency":0.94,"redundancy":0.82,"dependency_health":0.90},{"serve":0.90,"write":0.82}),
    RecoveryCheckpoint(4,{"capacity":0.96,"consistency":0.98,"redundancy":0.91,"dependency_health":0.95},{"serve":0.97,"write":0.93}),
    RecoveryCheckpoint(5,{"capacity":0.98,"consistency":0.99,"redundancy":0.94,"dependency_health":0.97},{"serve":0.99,"write":0.96}),
]

if __name__ == "__main__":
    ev = PhoenixEvaluator(reference,{"serve":1.0,"write":1.2})
    print(ev.evaluate_trajectory(trajectory,invariants,threshold=0.9,hold=2))
