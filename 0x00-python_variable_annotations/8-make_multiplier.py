#!/usr/bin/env python3
"""
task: 8. Complex types - functions
condition: mandatory
Write a type-annotated function make_multiplier that takes a float multiplier
as argument and returns a function that multiplies a float by multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    function to_kv >> makes a tuple from a key and value
        k: tuple key value >> str
        v: tupble value >> float or int
    return: tuple >> (str, float)
    """

    def amir(num: float) -> float:
        """
        amir: callable function
        """

        return float(num * multiplier)

    return amir
