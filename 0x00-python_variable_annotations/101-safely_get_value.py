#!/usr/bin/env python3
"""
Python Vaiable Annotaions presentation on code
"""
from typing import Mapping, Union, Any, TypeVar


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    Using the TypeVar from typing to set a
    not known type object
    """

    if key in dct:
        return dct[key]
    else:
        return default
