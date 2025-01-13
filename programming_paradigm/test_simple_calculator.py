
import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-6, 1), -5)
        # Add more assertions to thoroughly test the add method.

    def test_subtraction(self):
        """Test the addition method."""
        self.assertEqual(self.calc.subtract(-2, 3), -5)
        self.assertEqual(self.calc.subtract(17, 10), 7)
        self.assertEqual(self.calc.subtract(-6, 1), -7)
        # Add more assertions to thoroughly test the subtract method.

# Remember to write additional test methods for subtract, multiply, and divide.

    def test_multiply(self):
        """Test the addition method."""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        self.assertEqual(self.calc.multiply(-6, 1), -6)
        # Add more assertions to thoroughly test the multiply method.

    def test_divide(self):
        """Test the addition method."""
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertEqual(self.calc.divide(-7, 1), 7)
        self.assertEqual(self.calc.divide(-6, -3), 2)
        # Add more assertions to thoroughly test the divide method.