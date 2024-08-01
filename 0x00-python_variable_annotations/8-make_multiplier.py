#!/usr/bin/env python3
"""
Module for make_multiplier function
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Return a function that multiplies a float by multiplier
    """
    def multiply(x: float) -> float:
        return x * multiplier
    return multiply
