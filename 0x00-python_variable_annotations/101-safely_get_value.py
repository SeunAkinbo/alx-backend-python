#!/usr/bin/env python3
"""Module - 101-safely_get_value"""
from typing import Union, Mapping, Any, TypeVar

T = TypeVar("T")


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """The function returns the dictionary key"""
    if key in dct:
        return dct[key]
    else:
        return default
