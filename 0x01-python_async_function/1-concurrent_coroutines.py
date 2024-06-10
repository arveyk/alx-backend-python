#!/usr/bin/env python3
"""
Module for 1-concurrent_coroutine
"""
import asyncio
import random

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """ Function that waits for some second
    Args:
        n: some number
        max_delay: the maximum amount of time to wait
    Returns: amount of time it delayed
    """
    result_list = []
    for dly in range(max_delay):
        delay = await wait_random(max_delay)
        result_list.append(delay)
    return result_list
