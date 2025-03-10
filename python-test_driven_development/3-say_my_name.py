#!/usr/bin/python3
"""
This module provides a function that prints
"My name is <first name> <last name>" were
<first name> and <last name> must be strings
"""


def say_my_name(first_name, last_name=""):
    """
    function that prints:
    My name is <first name> <last name>
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))
