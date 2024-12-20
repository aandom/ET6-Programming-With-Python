#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 20 12 24

@author: Alexander Andom
"""

def mystery_1(a,b):
    """Adds two numbers and return the result 

    Parameters:
        a: int, any integer
        b: int, any integer
    
    Returns -> int the result of sum of the numbers a and b
    >>> mystery_1(1, 0)
    1

    >>> mystery_1(-1, 1)
    0

    >>> mystery_1(8, 19)
    27
    """
    assert isinstance(a, int), "first argument should be an integer"
    assert isinstance(b, int), "second argument should be an integer"
    return a + b
