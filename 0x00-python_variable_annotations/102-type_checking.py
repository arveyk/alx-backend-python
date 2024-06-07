#!/usr/bin/env python3
"""Module type checking concept
"""
from typing import Tuple


def zoom_array(lst: list, factor: int = 2) -> Tuple:
    """Function to zoom into a list by a given factor
    Args:
        lst: list of numbers to be zoomed
        factor: number of times to zoom in
    Returns: tuple of the factored list"""
    zoomed_in: Tuple = tuple([
        item for item in lst
        for i in range(factor)
    ])
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
