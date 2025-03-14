#!/usr/bin/python3
"""
Defines a class MyList that inherits from list.
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        list: A list of available attributes and methods of the object.
    """
    return dir(obj)
