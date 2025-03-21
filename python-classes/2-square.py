#!/usr/bin/python3
"""
Defines a class Square.
"""


class Square:
    """
    A class that defines a square by its size.
    With validation for the size attribute.

    Attributes:
    __size (int): The size of the square (private).
    """

    def __init__(self, size=0):
        """
        Initializes the square with a private instance attribute size.

        Args:
            size (int): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
