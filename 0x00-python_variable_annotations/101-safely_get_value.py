#!/usr/bin/env python3
"""Module for function 101-safely get value
"""
from typing import Any, Union, Mapping, TypeVar


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """Function to return member of a dict at a given key
    Args:
        dct: dictionary
        key: key to be used to access dct
        default: value to return if dct is not a dict
    Returns: value at dct[key], default if it fails
    """
    if key in dct:
        return dct[key]
    else:
        return default
