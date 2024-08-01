#!/usr/bin/env python3
"""
Module for safe_first_element function
"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Return the first element of the sequence or None if empty
    """
    if lst:
        return lst[0]
    else:
        return None
