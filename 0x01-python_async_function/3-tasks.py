#!/usr/bin/env python3
""" Module for running tasks
"""
import asyncio
from typing import Any
from typing import Awaitable

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Awaitable[Any]:
    """Task generating function
    Args:
        max_delay: maximum amount of time to delay
    Return: asyncio.Task
    """
    return asyncio.create_task(wait_random(max_delay))
