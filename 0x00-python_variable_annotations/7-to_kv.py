#!/usr/bin/python3
"""
Python Vaiable Annotaions presentation on code
"""
from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Annotaed function that power float | int and
    return a tuple (str, float)
    """
    return (k, v ** 2)
