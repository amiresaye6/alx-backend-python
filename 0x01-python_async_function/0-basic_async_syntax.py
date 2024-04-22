#!/usr/bin/env python3
"""
task: 0. The basics of async

condition: mandatory

required: Write an asynchronous coroutine that takes in an integer argument
(max_delay, with a default value of 10) named wait_random that waits for
a random delay between 0 and max_delay (included and float value) seconds and
eventually returns it.

Use the random module.
"""
import random


async def wait_random(max_delay=10):
    """
    wait_random: returns a random delay between 0 and max_delay
    max_delay: maximum avalibale delay (int)
    returns: (int)
    """

    return random.uniform(0, max_delay)
