#!/usr/bin/python3
"""
    Module defines a unitest for function:
    def max_integer(my_list=[]):
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInt(unittest.TestCase):
    """
    defines class to test the max integer function
    """


    def test_max_integer(self):
        """
        Tests the max integer in a list of integers or float for
        both positive or negative values
        """
        self.assertIsNone(max_integer([]))
        self.assertAlmostEqual(max_integer([4, 5, 6, 1, 2, 3, 2]), 6)
        self.assertAlmostEqual(max_integer([-4, -3, -2, -1, 0, 1, 2]), 2)
        self.assertAlmostEqual(max_integer([3.1]), 3.1)
        self.assertAlmostEqual(max_integer([10, -12, -150, 0]), 10)

    def test_wrong_types(self):
        """
        Tests the max integer with wrong non numeric data types
        """
        with self.assertRaises(TypeError):
            max_integer(["School", 9, "200", -9.7, None])
        with self.assertRaises(TypeError):
            max_integer(None)
