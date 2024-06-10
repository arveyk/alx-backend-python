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
        list_len = len(result_list)
        if list_len >= 1:
            if result_list[list_len - 1] > delay:
                temp = result_list[list_len - 1]
                result_list[list_len - 1] = delay
                result_list.append(temp)
            else:
                result_list.append(delay)
        else:
            result_list.append(delay)
    list.sort(result_list)
    return result_list
