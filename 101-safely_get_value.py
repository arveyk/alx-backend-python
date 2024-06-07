#!/usr/bin/env python3
"""Module for function 101-safely get value
"""
from typing import TypeVar


dct = TypeVar("dct", dict)
key = TypeVar("key", str)
default = TypeVar("default", None)

def safely_get_value(dct , key, default = None) -> dct[key] | default:
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
