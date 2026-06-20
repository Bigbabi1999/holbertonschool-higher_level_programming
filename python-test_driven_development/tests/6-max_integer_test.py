#!/usr/bin/python3
"""Unittest for max_integer"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest. TestCase):
    """Test cases for max_integer"""

    def test_empty_list(self):
        """Empty list"""
        self.assertIsNone(max_integer([]))

    def test_one_element(self):
        """One element"""
        self.assertEqual(max_integer([5]), 5)

    def test_positive_integer(self):
        """Positive integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_negative_integers(self):
        """Negative intgers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        """Mixed positive and negative"""
        self.assertEqual(max_integer([-10, 5, 2, 99, 4]), 99)

    def test_max_at_beginning(self):
        """Maximum at beginning"""
        self.assertEqual(max_integer([100, 2, 3, 4]), 100)

    def test_max_at_end(self):
        """Maximum at the end"""
        self.assertEqual(max_integer([1, 2, 3, 100]), 100)

    def test_duplicates(self):
        """Duplicate maximum values"""
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

    def test_float_values(self):
        """Float values"""
        self.assertEqual(max_integer([1.1, 2.2, 3.3]), 3.3)

    def test_string(self):
        """String input"""
        self.assertEqual(max_integer("Bello"), "o")

if __name__ == "__main__":
    unittest.main()