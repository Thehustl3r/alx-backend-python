#!/usr/bin/env python3
"""
use of type script in python
"""
from typing import TypeVar, Any, Union, Mapping


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[T, Any]:
    if key in dct:
        return dct[key]
    else:
        return default
