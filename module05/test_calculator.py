
import unittest
import calculator


class CalculatorTestCase(unittest.TestCase):
    """
    Unit testing of calculator program
    """
    def test_add(self):
        self.assertEqual(calculator.add(1, 1), 2)
        self.assertEqual(calculator.add(3, 4), 7)
        self.assertEqual(calculator.add(5, 6), 11)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(123, 3), 120)
        self.assertEqual(calculator.subtract(123, 3), 120)
        self.assertEqual(calculator.subtract(23, 10), 13)

    def test_multiply(self):
        self.assertEqual(calculator.multiply(2, 10), 20)
        self.assertEqual(calculator.multiply(6, 20), 120)
        self.assertEqual(calculator.multiply(4, 4), 16)

    def test_divide(self):
        self.assertEqual(calculator.divide(122, 2), 61)
        self.assertEqual(calculator.divide(20, 4), 5)
        self.assertEqual(calculator.divide(12, 2), 6)


if __name__ == "__main__":
    unittest.main()
