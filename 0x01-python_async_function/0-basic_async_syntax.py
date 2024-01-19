#!/usr/bin/env python3
"""
0-basic_async_syntax
"""
import random
import asyncio


async def wait_random(max_delay=10):
    """the function that generate a random number between 0 and max"""

    random_num = random.uniform(0, max_delay)
    await asyncio.sleep(random_num)
    res = random_num
    return res
