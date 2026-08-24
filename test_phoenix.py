import unittest
from phoenix import PhoenixEvaluator, RecoveryCheckpoint

class TestPhoenix(unittest.TestCase):
    def test_reference_has_full_fidelity(self):
        ref = {"a":1.0,"b":1.0}
        ev = PhoenixEvaluator(ref)
        self.assertAlmostEqual(ev.fidelity(ref),1.0)

    def test_bad_state_lower_fidelity(self):
        ref = {"a":1.0,"b":1.0}
        ev = PhoenixEvaluator(ref)
        self.assertLess(ev.fidelity({"a":0.2,"b":0.3}),1.0)

    def test_stable_hold_required(self):
        ref = {"a":1.0}
        ev = PhoenixEvaluator(ref)
        cps = [
            RecoveryCheckpoint(1,{"a":1.0},{"x":1.0}),
            RecoveryCheckpoint(2,{"a":0.4},{"x":0.4}),
            RecoveryCheckpoint(3,{"a":1.0},{"x":1.0}),
            RecoveryCheckpoint(4,{"a":1.0},{"x":1.0}),
        ]
        out = ev.evaluate_trajectory(cps,threshold=0.9,hold=2)
        self.assertEqual(out["recovery_time"],3)

if __name__ == "__main__":
    unittest.main()
