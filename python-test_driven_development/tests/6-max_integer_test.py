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
