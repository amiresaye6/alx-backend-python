#!/usr/bin/env python3
"""
task: 6. Complex types - mixed list

condition: mandatory
Write a type-annotated function sum_mixed_list which takes a list mxd_lst of
integers and floats and returns their sum as a float.
"""
from typing import List, Union
"""
List[int | float] is supported in 3.10+
"""


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    function sum_mixed_list >> sums a list of floot or int numbers
        input_list: list of float numbers list[float]
    return: sum of mxd_list >> float
    """
    res: float = 0.0

    for num in mxd_lst:
        res += num

    return res
