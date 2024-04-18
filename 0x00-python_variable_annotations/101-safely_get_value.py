#!/usr/bin/env python3
"""
task: 11. More involved type annotations
condition: #advanced
Given the parameters and the return values, add type annotations to
the function
"""
from typing import Mapping, Any, Union, TypeVar
T = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[Any, None] = None
                     ) -> Union[Any, None]:
    """
    Retrieve a value from a dictionary safely.

    Args:
        dct (Mapping): The dictionary to retrieve the value from.
        key (Any): The key to lookup in the dictionary.
        default (Union[Any, None], optional): The default value to return
        if the key is not found.
        Defaults to None.

    Returns:
        Union[Any, None]: The value corresponding to the key if found,
        otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
