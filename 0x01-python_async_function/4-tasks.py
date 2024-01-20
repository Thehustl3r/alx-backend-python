#!/usr/bin/env python3
"""
4-tasks.py
"""
import time
import asyncio
from typing import List
wait_n = __import__('1-concurrent_coroutines').wait_n
wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """the funciton that use random"""
    new_max_delay = await wait_random(max_delay)

    return await wait_n(n, new_max_delay)
