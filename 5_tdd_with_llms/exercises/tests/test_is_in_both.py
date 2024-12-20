#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 20 12 2024

@author: Alexander Andom
"""



import unittest

from ..is_in_both import is_in_both

class TestMyIsinboth(unittest.TestCase):
  """Test the is_in_both function."""

  def test_substring_in_both_strings(self):
      """Test that a substring present in both strings returns True."""
      self.assertEqual(is_in_both("hello", "hello world", "hello everyone"), True)

  def test_substring_not_in_second_string(self):
      """Test that a substring not present in both strings returns False."""
      self.assertEqual(is_in_both("python", "hello world", "hello everyone"), False)

  def test_empty_substring(self):
      """Test that an empty substring returns True when checked in both strings."""
      self.assertEqual(is_in_both("", "empty", "empty"), True)

  def test_substring_in_first_string_only(self):
      """Test that a substring present only in the first string returns False."""
      self.assertEqual(is_in_both("hello", "hello world", "goodbye everyone"), False)

  def test_substring_in_second_string_only(self):
      """Test that a substring present only in the second string returns False."""
      self.assertEqual(is_in_both("everyone", "hello world", "goodbye everyone"), False)

  def test_substring_in_both_empty_strings(self):
      """Test that an empty substring is present in both empty strings."""
      self.assertEqual(is_in_both("", "", ""), True)

if __name__ == "__main__":
    unittest.main()
