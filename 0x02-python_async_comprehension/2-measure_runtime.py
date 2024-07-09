#!/usr/bin/env python3
"""Module - 2-measure_runtime"""

import time
import asyncio
task = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """The measure_runtime function"""
    start = time.time()
    await asyncio.gather(task(), task(), task(), task())
    return time.time() - start
