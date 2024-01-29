#!/usr/bin/env python3
"""
use of type script in python
"""
from typing import Sequence, Any, Union, Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """fix annotation"""
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    # return tuple(zoomed_in)
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(tuple(array))

zoom_3x = zoom_array(tuple(array), 3)
