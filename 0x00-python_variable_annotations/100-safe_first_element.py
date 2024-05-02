#!/usr/bin/env python3
"""
Python Vaiable Annotaions presentation on code
"""
from typing import Sequence, Union, Any


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Using the TypeVar from typing to set a
    not known type object
    """

    if lst:
        return lst[0]
    else:
        return None
