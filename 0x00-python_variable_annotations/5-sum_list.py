#!/usr/bin/env python3
"""
task: 5. Complex types - list of floats
condition: mandatory
Write a type-annotated function sum_list which takes a list input_list of
floats as argument and returns their sum as a float.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    function sum_list >> sums a list of floot numbers
        input_list: list of float numbers list[float]
    return: sum of input_list >> float
    """
    sumRes: float = 0.0

    for num in input_list:
        sumRes += num

    return sumRes
