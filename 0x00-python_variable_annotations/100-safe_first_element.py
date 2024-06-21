#!/usr/bin/env python3
"""Module to explore Duck-typing
"""
from typing import Any, Sequence, Union

def safe_first_element(lst: Sequence[Any]) -> Union[Any,  None]:
    """Function to demo ducktyping
    Args:
        lst: list variable
    Returns: first element if lst can be suscripted, None if not
    """
    if lst:
        return lst[0]
    else:
        return None
