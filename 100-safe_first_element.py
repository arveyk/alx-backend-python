#!/usr/bin/env python3
"""Module to explore Duck-typing
"""

def safe_first_element(lst: any) -> any | None:
    """Function to demo ducktyping
    """
    if lst:
        return lst[0]
    else:
        return None
