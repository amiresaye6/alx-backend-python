#!/usr/bin/env python3
"""
task: 3. Tasks

condition: mandatory
Import wait_random from 0-basic_async_syntax.

Write a function (do not create an async function, use the regular function
syntax to do this) task_wait_random that takes an integer max_delay and
returns a asyncio.Task.
"""
from asyncio import create_task, Task

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """
    task_wait_random: returns a random delay between 0 and max_delay
    max_delay: maximum avalibale delay (int)
    returns: (int)
    """

    return create_task(wait_random(max_delay))
