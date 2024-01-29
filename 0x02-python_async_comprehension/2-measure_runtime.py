#!/usr/bin/env python3
"""./2-measurement-py"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """async function that will return the array """
    start_time = time.perf_counter()
    await asyncio.gather(async_comprehension())
    end_time = time.perf_counter()
    return end_time - start_time
