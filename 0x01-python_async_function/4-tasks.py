#!/usr/bin/env python3
""" Async Function
"""
from typing import List
import asyncio
import time


task_wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:

    """ Function that masures the time it takes to execute a function
    Args:
        n: some number
        max_delay: the maximum amount of time to wait
    Returns: amount of time used
    """
    result_list = []
    list_fin = []
    for dly in range(n):
        delay = await task_wait_random(max_delay)
        list_len = len(result_list)
        result_list.append(delay)
    length = len(result_list)
    for i in range(length):
        small = result_list[0]
        for i in (result_list):
            if i < small:
                small = i
        list_fin.append(small)
        result_list.remove(small)
    return list_fin
