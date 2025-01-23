import unittest
from programming_paradigm.simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = SimpleCalculator()

    def test_add(self):
        self.assertEqual(self.calculator.add(1, 2), 3)

    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(2, 1), 1)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(2, 3), 6)

    def test_divide(self):
        self.assertEqual(self.calculator.divide(6, 2), 3)
        self.assertIsNone(self.calculator.divide(6, 0))
        # self.assertRaises(ValueError, self.calculator.divide, 6, 0)
if __name__ == '__main__':
    unittest.main()