#!/usr/bin/env python3
"""./0-async_generator"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator:
    """async function that will wait random time"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
