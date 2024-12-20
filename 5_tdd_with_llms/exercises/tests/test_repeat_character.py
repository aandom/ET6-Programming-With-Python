#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 20 12 2024

@author: Alexander Andom
"""

import unittest

from ..repeat_character import repeat_character  


class TestMyRepeatCharacter(unittest.TestCase):
    """Test the repeat_character function."""

    def test_repeat_single_occurrence(self):
        """Test that a single occurrence of the character is repeated correctly."""
        self.assertEqual(repeat_character("hello", "o", 3), "hellooo")

    def test_repeat_multiple_occurrences(self):
        """Test that multiple occurrences of the character are repeated correctly."""
        self.assertEqual(repeat_character("hello world", "o", 2), "helloo woorld")

    def test_repeat_no_occurrences(self):
        """Test that if the character doesn't appear, the string remains unchanged."""
        self.assertEqual(repeat_character("hello world", "z", 3), "hello world")

    def test_repeat_with_empty_string(self):
        """Test that an empty string returns an empty string."""
        self.assertEqual(repeat_character("", "o", 3), "")

    def test_repeat_single_character(self):
        """Test repeating a character in a string of length 1."""
        self.assertEqual(repeat_character("a", "a", 5), "aaaaa")

    def test_invalid_char(self):
        """Test that an assertion error is raised when the character is not a single character string."""
        with self.assertRaises(AssertionError):
            repeat_character("hello", "hello", 3)

    def test_invalid_n(self):
        """Test that an assertion error is raised when n is not a positive integer."""
        with self.assertRaises(AssertionError):
            repeat_character("hello", "o", -1)

    def test_repeat_character_with_large_n(self):
        """Test repeating a character with a large number."""
        self.assertEqual(repeat_character("hello", "o", 100), "hell" + "o" * 100)

if __name__ == '__main__':
    unittest.main()
