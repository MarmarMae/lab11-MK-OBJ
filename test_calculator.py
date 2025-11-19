# https://github.com/MarmarMae/lab11-MK-OBJ
# Partner 1: Marley Kight
# Partner 2:
import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(subtract(1, 1), 0)
        self.assertEqual(subtract(-2, 1), -3)
        self.assertEqual(subtract(2, -1), 3)

    def test_divide_by_zero(self):
        b = div(self.b)
        self.assertFalse(b == 0)

    def test_logarithm(self):
        self.assertEqual(logarithm(2, 2), 1)
        self.assertEqual(logarithm(4, 2), 2)
        self.assertEqual(logarithm(2, 4), 0.5)

    def test_log_invalid_base(self):
        b = logarithm(self.b)
        self.assertFalse(b == 0)
        self.assertFalse(b <= 0)

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(1,2), 2)
        self.assertEqual(mul(20, 8), 160)
        self.assertEqual(mul(-20, 8), -160)


    def test_divide(self): # 3 assertions
        self.assertEqual(div(2, 1), 2)
        self.assertEqual(div(20, 5), 4)
        self.assertEqual(div(600000, 1), 600000)
        self.assertEqual(div(-40, 5), -8)
        self.assertEqual(div(-30,-6), 5)


    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(5, 0)

    def test_logarithm(self): # 3 assertions I (Marley) wrote this idk
        self.assertEqual(logarithm(8,2),3)
        self.assertNotEqual(logarithm(8,2),4)
        self.assertNotEqual(logarithm(8,2),5)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(5,1)
            
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 5)


    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(5, 12), 13)
        self.assertNotEqual(hypotenuse(6, 8), 9)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-4)
        self.assertEqual(square_root(16), 4)
        self.assertEqual(square_root(4), 2)
        self.assertNotEqual(square_root(4), 1)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()
