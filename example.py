from phoenix import PhoenixEvaluator, RecoveryCheckpoint

reference = {
    "service_health":1.0,
    "consistency":1.0,
    "redundancy":1.0
}

checkpoints = [
    RecoveryCheckpoint(1,{"service_health":0.6,"consistency":0.7,"redundancy":0.5},{"core":0.6}),
    RecoveryCheckpoint(2,{"service_health":0.9,"consistency":0.95,"redundancy":0.85},{"core":0.9}),
    RecoveryCheckpoint(3,{"service_health":0.97,"consistency":0.99,"redundancy":0.92},{"core":0.97}),
]

invariants = [
    lambda s: s["consistency"] >= 0.95,
    lambda s: s["redundancy"] >= 0.85
]

print(PhoenixEvaluator(reference).evaluate_trajectory(
    checkpoints,
    invariants,
    threshold=0.88,
    hold=2
))
