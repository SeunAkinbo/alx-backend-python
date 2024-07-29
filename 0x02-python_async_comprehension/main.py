#!/usr/bin/env python3

from typing import Generator
from time import sleep

# def generate() -> Generator[int, None, None]:
#     """The function returns a generator"""
#     for i in range(10):
#         yield i
#         sleep(3)
        

# for i in generate():
#     print(i, end=',')

# import asyncio

# async_generator = __import__('0-async_generator').async_generator

# async def print_yielded_values():
#     result = []
#     async for i in async_generator():
#         result.append(i)
#     print(result)

# asyncio.run(print_yielded_values())

import asyncio

# async_comprehension = __import__('1-async_comprehension').async_comprehension


# async def main():
#     print(await async_comprehension())

# asyncio.run(main())

measure_runtime = __import__('2-measure_runtime').measure_runtime


async def main():
    return await(measure_runtime())

print(
    asyncio.run(main())
)