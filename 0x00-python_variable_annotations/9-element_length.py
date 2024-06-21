#!/usr/bin/env python3
"""Module to explore duck typing
"""
from typing import Sequence, List, Tuple, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Function that return the length of an iterable
    Args:
        lst: list whose length is to be evaluated
    Returns: the list length
    """
    return [(i, len(i)) for i in lst]
