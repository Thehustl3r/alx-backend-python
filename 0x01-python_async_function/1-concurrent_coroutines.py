#!/usr/bin/env python3
"""
1-concurent_coroutines.py
"""
import random
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: float, max_delay: float) -> float:
    """the function that generate a random number and save them in the list"""

    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]

    return [await task for task in asyncio.as_completed(tasks)]
