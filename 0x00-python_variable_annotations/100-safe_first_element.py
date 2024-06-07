#!/usr/bin/env python3
"""Module to explore Duck-typing
"""


def safe_first_element(lst: any) -> any | None:
    """Function to demo ducktyping
    Args:
        lst: list variable
    Returns: first element if lst can be suscripted, None if not
    """
    if lst:
        return lst[0]
    else:
        return None
