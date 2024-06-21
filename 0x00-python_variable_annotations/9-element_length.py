#!/usr/bin/env python3
"""Module to explore duck typing
"""
from typing import Sequence, List, Tuple


def element_length(lst: List[int]) -> List[Tuple[Sequence, int]]:
    """Function that return the length of an iterable
    Args:
        lst: list whose length is to be evaluated
    Returns: the list length
    """
    return [(i, len(i)) for i in lst]
