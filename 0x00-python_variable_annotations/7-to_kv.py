#!/usr/bin/env python3
"""Module to define function for returning a tuple made up of
the arguments it is supplied
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Function that returns a tuple consisting of the arguments it is
    supplied
    Args:
       k: the 'key' of the tuple
       v: the number to be supplied
    Returns: a tupple"""

    tup = (k, v * v)
    return tup
