#!/usr/bin/env python3
"""
task: 2. Basic annotations - floor
condition: mandatory
required: Write a type-annotated function floor which takes a float n as
argument and returns the floor of the float.
"""
import math


def floor(n: float) -> int:
    """
    function floor >> floors a float numbwer
        n: the floot number to be floored
    return: floor(n) >> int
    """

    return math.floor(n)
