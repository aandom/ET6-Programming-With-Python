#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 20 12 2024

@author: Alexander Andom
"""

import unittest

from ..is_in_one import is_in_one

class TestMyIsinone(unittest.TestCase):
    """Test the is_in_one function."""

    def test_substring_in_first_only(self):
        """Test that the substring in the first string only returns True."""
        self.assertTrue(is_in_one("hello", "hello world", "goodbye everyone"))

    def test_substring_in_second_only(self):
        """Test that the substring in the second string only returns True."""
        self.assertTrue(is_in_one("everyone", "goodbye world", "hello everyone"))

    def test_substring_in_both_strings(self):
        """Test that the substring in both strings returns False."""
        self.assertFalse(is_in_one("world", "hello world", "goodbye world"))

    def test_substring_in_neither_string(self):
        """Test that the substring in neither string returns False."""
        self.assertFalse(is_in_one("python", "hello world", "goodbye everyone"))

    def test_empty_substring(self):
        """Test that an empty substring is considered in both strings, returning False."""
        self.assertFalse(is_in_one("", "non-empty", "non-empty"))

    def test_substring_in_first_empty_second(self):
        """Test that a substring in the first string and an empty second string returns True."""
        self.assertTrue(is_in_one("hello", "hello world", ""))

    def test_substring_in_second_empty_first(self):
        """Test that a substring in the second string and an empty first string returns True."""
        self.assertTrue(is_in_one("world", "", "hello world"))

if __name__ == "__main__":
    unittest.main()
