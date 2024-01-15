#!/usr/bin/env python3
from typing import List, Union
"""
use of type script in python
"""


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Return the sum of the list.

    Parameters:
    - mxd_lst List[Union[int, float]]: The list

    Returns:
    float: The result of the sum.
    """
    return sum(mxd_lst)
