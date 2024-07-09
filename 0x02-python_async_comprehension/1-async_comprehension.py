#!/usr/bin/env python3
"""Module - 1- async_comprehension"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """The async_comprehension function"""
    return [_ async for _ in async_generator()]
