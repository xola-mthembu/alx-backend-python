#!/usr/bin/env python3
"""
Module for sum_mixed_list function
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Return the sum of a mixed list of integers and floats
    """
    return sum(mxd_lst)
