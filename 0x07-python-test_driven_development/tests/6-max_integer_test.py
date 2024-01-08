#!/usr/bin/python3
"""
This files provides unittests for the module '6-max_integer'
"""
import unittest
max_integer = __import__('6-max_integer').max_integer
class TestMaxInteger(unittest.TestCase):
    """TestCase subclass for unittests"""

    def test_max_integer(self):
        """perform tests for edge cases"""
        
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([2]), 2)
        self.assertEqual(max_integer([-5]), -5)
        self.assertEqual(max_integer([-7, -2, -3]), -2)
        self.assertEqual(max_integer([70, 5, 10]), 70)
        self.assertEqual(max_integer([23, 2, 87, 34, 87]), 87)
        self.assertEqual(max_integer([55, 55, 55]), 55)
        
    def test_type_errors(self):
        """type_errors"""
        self.assertRaises(TypeError, max_integer, ["bkz", 3])
        self.assertRaises(TypeError, max_integer, [[7, 3], 9])
