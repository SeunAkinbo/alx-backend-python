#!/usr/bin/env python3
"""1-concurrent_coroutines"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """wait_n function
    """
    result = []
    while n:
        delay = await wait_random(max_delay)
        result.append(delay)
        n -= 1
    return sorted(result)
