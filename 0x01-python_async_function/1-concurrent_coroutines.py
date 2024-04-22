#!/usr/bin/env python3
"""
task: 1. Let's execute multiple coroutines at the same time with async

condition: mandatory

Import wait_random from the previous python file that you’ve written and write
an async routine called wait_n that takes in 2 int arguments (in this order):
n and max_delay. You will spawn wait_random n times with the specified
max_delay.

wait_n should return the list of all the delays (float values). The list of
the delays should be in ascending order without using sort() because of
concurrency.
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    wait_n: funciton waits for n times using the random value generated from
    wait_random(max_delay)
    n: times of runnit wait_random() function
    max_delay: the maximum delay possible from wait_random() function

    returns: list of all floating point delays List[float]
    """
    waits = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]

    return [await task for task in asyncio.as_completed(waits)]
