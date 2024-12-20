#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 20 12 2024

@author: Alexander Andom
"""


# """ Is in one

# Write a function that takes in a string and two lists of strings. 
# It will return true if the item is in _only one_ of the lists.

# """

def is_in_one(tofind: str , str_one: str, str_two: str):
  """Checks if a substring is present in only one of the provided strings.

  Parameters:
      tofind: str, the substring to search for
      str_one: str, the first string to check
      str_two: str, the second string to check
  
  Returns -> bool: True if the substring is found in only one of the strings, otherwise False

  Examples:
    >>> is_in_one("hello", "hello world", "hello everyone")
    False

    >>> is_in_one("python", "python world", "hello everyone")
    True

    >>> is_in_one("", "empty", "empty")
    False
  """
  return ((tofind in str_one and tofind not in str_two) or  (tofind not in str_one and tofind in str_two))
  # return (tofind in str_one) != (tofind in str_two)
