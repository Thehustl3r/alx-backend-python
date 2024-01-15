#!/usr/bin/env python3
"""
use of type script in python to manage the
variables
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Return the sum of the list.

    Parameters:
    - input_list (float): The numerator.

    Returns:
    float: The result of the sum.
    """
    return sum(input_list)
