#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 20 12 24

@author: Alexander Andom
"""

import unittest

from ..mystery_1 import mystery_1

class TestMystery1(unittest.TestCase):
    """Test the mystery_1 function"""

    def test_0_and_0(self):
        """it should return 0"""
        self.assertEqual(mystery_1(0, 0), 0)

    def test_0_and_negative_1(self):
        """it should return -1"""
        self.assertEqual(mystery_1(0, -1), -1)

    def test_2_and_4(self):
        """it should return 6"""
        self.assertEqual(mystery_1(2, 4), 6)

    def test_10_and_10(self):
        """it should return 20"""
        self.assertEqual(mystery_1(10, 10), 20)

    def test_8_and_negative_15(self):
        """it should return -7"""
        self.assertEqual(mystery_1(8, -15), -7)

    def test_1_and_negative_1(self):
        """it should return 0"""
        self.assertEqual(mystery_1(1, -1), 0)

    def test_1_and_two(self):
        """it should raise an assertion error if the we non integer arguments"""
        with self.assertRaises(AssertionError):
                mystery_1(1,"two")
        # self.assertEqual(mystery_1(1, "two"), 0)
