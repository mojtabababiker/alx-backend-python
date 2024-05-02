#!/usr/bin/python3
"""
Python Vaiable Annotaions presentation on code
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Annotaed function that sum a list of float and return
    the value as float
    """
    sum: float = 0.0
    for num in input_list:
        sum += num

    return sum
