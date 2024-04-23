#!/usr/bin/env python3
"""
task: 2. Run time for four parallel comprehensions

condition: mandatory

Import async_comprehension from the previous file and write a measure_runtime
coroutine that will execute async_comprehension four times in parallel using
asyncio.gather.
measure_runtime should measure the total runtime and return it.
Notice that the total runtime is roughly 10 seconds, explain it to yourself.
"""
from typing import List
from time import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    generates a random float numbers list and waits for a second.

    Parameters:
    - None.

    Returns:
    - List[float]: Returns a list of float random numbers between 0 and 10.
    """

    start_time = time()

    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)
    return time() - start_time
