import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Test cases for SimpleCalculator class."""

    def setUp(self):
        """Set up a calculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test addition operation with various inputs."""
        self.assertEqual(self.calc.add(2, 3), 5)        # Positive numbers
        self.assertEqual(self.calc.add(-1, 1), 0)        # Negative and positive
        self.assertEqual(self.calc.add(0, 0), 0)         # Zeros
        self.assertEqual(self.calc.add(2.5, 3.5), 6.0)   # Floats
        self.assertEqual(self.calc.add(-5, -3), -8)      # Negative numbers

    def test_subtraction(self):
        """Test subtraction operation with various inputs."""
        self.assertEqual(self.calc.subtract(5, 3), 2)    # Positive numbers
        self.assertEqual(self.calc.subtract(3, 5), -2)    # Reversed order
        self.assertEqual(self.calc.subtract(0, 0), 0)     # Zeros
        self.assertEqual(self.calc.subtract(-1, -1), 0)   # Negative numbers
        self.assertEqual(self.calc.subtract(5.5, 2.5), 3.0)  # Floats

    def test_multiplication(self):
        """Test multiplication operation with various inputs."""
        self.assertEqual(self.calc.multiply(2, 3), 6)     # Positive numbers
        self.assertEqual(self.calc.multiply(-2, 3), -6)    # Negative and positive
        self.assertEqual(self.calc.multiply(0, 5), 0)      # Zero multiplication
        self.assertEqual(self.calc.multiply(2.5, 4), 10.0) # Floats
        self.assertEqual(self.calc.multiply(-3, -4), 12)   # Negative numbers

    def test_division(self):
        """Test division operation with various inputs."""
        self.assertEqual(self.calc.divide(6, 3), 2)       # Exact division
        self.assertEqual(self.calc.divide(5, 2), 2.5)      # Fractional result
        self.assertEqual(self.calc.divide(-6, 3), -2)      # Negative numerator
        self.assertEqual(self.calc.divide(6, -3), -2)      # Negative denominator
        self.assertEqual(self.calc.divide(0, 5), 0)        # Zero numerator
        self.assertEqual(self.calc.divide(1, 3), 1/3)      # Fraction result

    def test_division_by_zero(self):
        """Test division by zero returns None."""
        self.assertIsNone(self.calc.divide(5, 0))         # Division by zero
        self.assertIsNone(self.calc.divide(-5, 0))        # Negative division by zero
        self.assertIsNone(self.calc.divide(0, 0))         # Zero division by zero

if __name__ == '__main__':
    unittest.main()