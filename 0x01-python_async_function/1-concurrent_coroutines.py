#!/usr/bin/env python3
"""
Module for 1-concurrent_coroutine
for executing multiple coroutines
"""

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """ Function that waits for some second
    Args:
        n: some number
        max_delay: the maximum amount of time to wait
    Returns: amount of time it delayed
    """
    result_list = []
    for dly in range(n):
        delay = await wait_random(max_delay)
        result_list.append(delay)

    final = []
    while result_list:
        smallest = result_list[0]
        for num in result_list:
            if num < smallest:
                smallest = num
            final.append(small)
            result_list.remove(small)
    return result_list
