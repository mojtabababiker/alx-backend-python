#!/usr/bin/env python3
"""
Interducing async approach in pytyon
"""
import random
import asyncio


async def wait_random(max_delay: int = 10):
    """
     asynchronous coroutine that takes in an integer argument
    (max_delay, with a default value of 10), and waits for
    a random delay between 0 and max_delay
    (included and float value) seconds returns it.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
