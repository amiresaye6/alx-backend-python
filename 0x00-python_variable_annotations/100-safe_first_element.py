#!/usr/bin/env python3
"""
task: 10. Duck typing - first element of a sequence
condition: #advanced
Augment the following code with the correct duck-typed annotations:
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    function gets the first elment of a list
    lst: the list we need its first elment
    return: list
    """
    if lst:
        return lst[0]
    else:
        return None
