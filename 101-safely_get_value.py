#!/usr/bin/env python3
"""Module for function 101-safely get value
"""
from typing import TypeVar


dct = TypeVar("dct", dict)
key = TypeVar("key", str)
default = TypeVar("default", None)

def safely_get_value(dct , key, default = None) -> dct[key] | default:
    """
    """
    if key in dct:
        return dct[key]
    else:
        return default
