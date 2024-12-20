#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 20 12 2024

@author: Alexander Andom
"""


# """ Is in

# Write a function that takes in a string and two lists of strings. 
# It will return true if the item is in _at least one_ of the lists.

# """


def is_in(tofind: str , list_one: list , list_two: list):
  """Checks if a string is present in only one of the provided strings.

  Parameters:
      tofind: str, the string to search for
      list_one: list, the first list of strings to check
      list_two: list, the second list of strings to check
  
  Returns -> bool: True if the string is found in one of the list of strings, otherwise False

  Raises:
    ValueError: If 'tofind' is not a string.
    ValueError: If 'list_one' is not a list of strings.
    ValueError: If 'list_two' is not a list of strings.

  Examples:
    >>> is_in("hello", ["hello", "world"], ["hello", "everyone"])
    True

    >>> is_in("python", ["python", "world"], ["hello", "everyone"])
    True

    >>> is_in("", [], [])
    False
  """
  assert isinstance(tofind, str), "The 'tofind' parameter must be a string."
  assert isinstance(list_one, list) and all(isinstance(item, str) for item in list_one), "The 'list_one' parameter must be a list of strings."
  assert isinstance(list_two, list) and all(isinstance(item, str) for item in list_two), "The 'list_two' parameter must be a list of strings."

  return (tofind in list_one or tofind in list_two)
