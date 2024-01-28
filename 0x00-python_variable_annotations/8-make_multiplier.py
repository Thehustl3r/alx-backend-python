#!/usr/bin/env python3
"""
use of type script in python
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """return a tuple"""
    def multiplier_function(x: float) -> float:
        return x * multiplier

    return multiplier_function
