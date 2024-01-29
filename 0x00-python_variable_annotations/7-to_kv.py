#!/usr/bin/env python3
"""
use of type script in python
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """return a tuple"""
    return k, float(v**2)
