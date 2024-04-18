#!/usr/bin/env python3
"""
task: 9. Let's duck type an iterable object
condition: mandatory
Annotate the below function’s parameters and return values with the
appropriate types
"""
from typing import Tuple, List, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]
