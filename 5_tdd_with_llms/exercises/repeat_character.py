#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 20 12 2024

@author: Alexander Andom
"""



# """ Repeat Character

# Write a function that takes in a string, a single character, and a number. 
# The function returns a string with each occurrence of the character repeated n times.

# """


def repeat_character(input_str: str, char_to_repeat: str, n: int) -> str:
  """Repeats each occurrence of a specified character in a string.

  Parameters:
      input_str: str, The string in which to repeat the character.
      char_to_repeat: str, The character to repeat.
      n: int, The number of times to repeat the specified character.

  Returns:
      str: A new string with each occurrence of `char` repeated `n` times.

  Raises:
      AssertionError: If `char_to_repeat` is not a single char_to_repeatacter string.
      AssertionError: If `char_to_repeat` is not a string.
      AssertionError: If `input_str` is not a string.
      AssertionError: If `n` is not a positive integer.

  Examples:
      >>> repeat_character("hello world", "o", 3)
      'hellooo wooorld'

      >>> repeat_character("python programming", "o", 2)
      'pythoon proogramming'

      >>> repeat_character("abcdef", "e", 4)
      'abcdeeeef'
  """
  assert len(char_to_repeat) == 1, "The 'char' parameter must be a single character string."
  assert isinstance(char_to_repeat, str), "The 'char' parameter must be a string."
  assert isinstance(input_str, str), "The 'input_str' parameter must be a string."
  assert isinstance(n, int) and n > 0, "The 'n' parameter must be a positive integer."

  
  result = ""

  for ch in input_str:
      # if ch == char_to_repeat:
      #     result += ch * n
      # else:
      #     result += ch
      result += (ch * n if ch == char_to_repeat else ch)

  return result
