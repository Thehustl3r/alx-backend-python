#!/usr/bin/env python3
"""./1-async_comprehension"""
import asyncio
import random
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """async function that will return the array of generated code"""
    return [num async for num in async_generator()]
