#!/usr/bin/env python3
"""
task: 4. Tasks
condition: mandatory

Take the code from and alter it into a new function task_wait_n. The
code is nearly identical to wait_n except task_wait_random is being called.
"""
from asyncio import create_task, as_completed
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    wait_n: funciton waits for n times using the random value generated from
    wait_random(max_delay)
    n: times of runnit wait_random() function
    max_delay: the maximum delay possible from wait_random() function

    returns: list of all floating point delays List[float]
    """

    tasks = [task_wait_random(max_delay) for _ in range(n)]

    return [await task for task in as_completed(tasks)]
