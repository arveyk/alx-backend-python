#!/usr/bin/env python3
"""
Module for 1-concurrent_coroutine
for executing multiple coroutines
"""
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
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

    length = len(result_list)
    for i in range(length):
        for k in range(i + 1, length):
            if result_list[i] > result_list[k]:
                result_list[i],  result_list[k] =\
                        result_list[k], result_list[i]
    return result_list
