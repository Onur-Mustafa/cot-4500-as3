import unittest
from src.main.assignment_3 import euler_method, runge_kutta_method, f

class TestNumericalMethods(unittest.TestCase):
    def test_euler_method(self):
        result = euler_method(f, 0, 1, 0.2, 10)
        self.assertAlmostEqual(result, 1.2446380979332121, places=10)
    
    def test_runge_kutta_method(self):
        result = runge_kutta_method(f, 0, 1, 0.2, 10)
        self.assertAlmostEqual(result, 1.251316587879806, places=10)

if __name__ == '__main__':
    unittest.main() 