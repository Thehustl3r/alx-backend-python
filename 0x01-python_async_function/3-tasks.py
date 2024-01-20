#!/usr/bin/env python3
"""
3-tasks.py
"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """the function that measures the total execution time"""
    start_time = time.time()
    # asyncio.run(wait_n(n, max_delay))
    await wait_n(n, max_delay)

    end_time = time.time()

    total_time = end_time - start_time

    return total_time / n
