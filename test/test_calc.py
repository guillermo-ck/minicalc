import unittest
from calc import add, subtract, power, divide

class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_power(self):
        self.assertEqual(power(2, 3), 8)

    def test_basic_division(self):
        self.assertEqual(divide(10, 2), 5)