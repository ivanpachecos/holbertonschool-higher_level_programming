#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    """
        Test for max integer function
    """

    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 5, 3]), 5)

    def test_none(self):
        self.assertIsNone(max_integer([]))

    def max_at_the_end(self):
        self.max_at_the_end([1, 2, 3, 4, 5], 5)

if __name__ == '__main__':
    unittest.main()
