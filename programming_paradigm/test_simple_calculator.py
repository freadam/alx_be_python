import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(2, 1), 1)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)

    def test_division(self):
        self.assertEqual(self.calc.divide(6, 2), 3)
        self.assertIsNone(self.calc.divide(6, 0))
        
if __name__ == '__main__':
    unittest.main()