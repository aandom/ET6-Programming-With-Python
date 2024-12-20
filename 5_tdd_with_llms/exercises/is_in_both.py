#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 20 12 2024

@author: Alexander Andom
"""



# """ Is in Both

# Write a function that takes in a string and two lists of strings. 
# It will return true if the item is in _both_ of the lists.

# """


def is_in_both(tofind: str , str_one: str, str_two: str):
  """Checks if a substring is present in both of the provided strings.

  Parameters:
      tofind: str, the substring to search for
      str_one: str, the first string to check
      str_two: str, the second string to check
  
  Returns -> bool: True if the substring is found in both strings, otherwise False

  Examples:
    >>> is_in_both("hello", "hello world", "hello everyone")
    True

    >>> is_in_both("python", "hello world", "hello everyone")
    False

    >>> is_in_both("", "empty", "empty")
    True
  """
  return (tofind in str_one and tofind in str_two)
