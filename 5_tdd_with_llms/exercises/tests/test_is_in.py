#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 20 12 2024

@author: Alexander Andom
"""

import unittest

from ..is_in import is_in

class TestMyIsInFunction(unittest.TestCase):
    """Test the is_in function."""

    def test_found_in_first_list_only(self):
      """Test that a string present in the first list returns True."""
      result = is_in("python", ["python", "world"], ["hello", "everyone"])
      self.assertTrue(result)

    def test_found_in_second_list_only(self):
      """Test that a string present in the second list returns True."""
      result = is_in("hello", ["world", "python"], ["hello", "everyone"])
      self.assertTrue(result)

    def test_found_in_both_lists(self):
      """Test that a string present in both lists returns True."""
      result = is_in("hello", ["hello", "world"], ["hello", "everyone"])
      self.assertTrue(result)

    def test_found_in_neither_list(self):
      """Test that a string present in neither list returns False."""
      result = is_in("java", ["python", "world"], ["hello", "everyone"])
      self.assertFalse(result)

    def test_empty_lists(self):
      """Test that an empty list returns False when the string is not in the list."""
      result = is_in("python", [], [])
      self.assertFalse(result)

    def test_empty_string_to_find(self):
      """Test that an empty string returns False when both lists are empty."""
      result = is_in("", [], [])
      self.assertFalse(result)

    def test_input_validation(self):
      """Test that invalid inputs raise an AssertionError."""
      with self.assertRaises(AssertionError):
          is_in("python", "not_a_list", ["hello", "world"])
      with self.assertRaises(AssertionError):
          is_in("python", ["hello", 1], ["world"])
      with self.assertRaises(AssertionError):
          is_in(123, ["hello", "world"], ["hello"])

if __name__ == '__main__':
    unittest.main()
