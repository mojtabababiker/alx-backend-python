#!/usr/bin/env python3
"""
Coroutine that collect 10 random number between 0 and 10
"""
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collect 10 random number between 0 and 10
    """
    return [val async for val in async_generator()]
