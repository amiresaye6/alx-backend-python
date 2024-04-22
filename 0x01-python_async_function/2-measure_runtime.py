#!/usr/bin/env python3
"""
task: 2. Measure the runtime

condition: mandatory
From the previous file, import wait_n into 2-measure_runtime.py.

Create a measure_time function with integers n and max_delay as arguments
that measures the total execution time for wait_n(n, max_delay), and returns
total_time / n. Your function should return a float.

Use the time module to measure an approximate elapsed time.
"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    measure_time: measures the total execution time for wait_n(n, max_delay)
    n: times of repeatation (int)
    max_delay: maximum delay possible from wait_random(max_delay) (int)

    returns: avrage processing time of wait_n() in seconds (float)
    """
    total_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    return (time.time() - total_time) / n
