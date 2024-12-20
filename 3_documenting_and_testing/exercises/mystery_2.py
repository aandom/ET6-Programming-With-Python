#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 20 12 2024

@author: Alexander Andom
"""



def mystery_2(a):
    """Returns the length of the input if it is non-empty.

    Parameters:
        a: Any iterable (e.g., list, string, tuple).

    Returns:
        int: The length of the iterable `a`, or None if `a` is empty.

    Examples:
        >>> mystery_2("hello")
        5

        >>> print(mystery_2([]))
        None

        >>> mystery_2([1, 2, 3])
        3
    """
    if len(a) == 0:
        return None

    return len(a)
