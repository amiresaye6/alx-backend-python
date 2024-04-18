#!/usr/bin/env python3
"""
task: 7. Complex types - string and int/float to tuple
condition: mandatory
Write a type-annotated function to_kv that takes a string k and an int OR
float v as arguments and returns a tuple. The first element of the tuple is
the string k. The second element is the square of the int/float v and should
be annotated as a float.
"""
from typing import Union, Tuple
"""
List[int | float] is supported in 3.10+
"""


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    function to_kv >> makes a tuple from a key and value
        k: tuple key value >> str
        v: tupble value >> float or int
    return: tuple >> (str, float)
    """

    return (k, float(v**2))
