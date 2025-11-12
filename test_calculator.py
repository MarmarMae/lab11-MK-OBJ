import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

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
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            log(0, 5)


    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(5, 12), 13)
        self.assertNotEqual(hypotenuse(6, 8), 9)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-4)
        self.assertEqual(square_root(16), 4)
        self.assertAlmostEqual(square_root(2.25), 1.5)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()