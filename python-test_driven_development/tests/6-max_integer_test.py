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

    def test_max_at_the_end(self):
        self.assertEqual(max_integer([1, 2, 4, 5]), 5)

    def test_max_at_the_beginning(self):
        self.assertEqual(max_integer([12, 4, 5, 3, 1]), 12)

if __name__ == '__main__':
    unittest.main()
