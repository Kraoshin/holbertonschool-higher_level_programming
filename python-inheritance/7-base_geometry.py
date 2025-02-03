#!/usr/bin/python3
"""Defines an empty class BaseGeometry."""


class BaseGeometry:
    """
    A base class for geometry-related operations.

    Methods:
        area(self): Raises an Exception indicating that the method
        is not implemented.
        integer_validator(self, name, value): Validates that value
        is a positive integer.
    """

    def area(self):
        """
        Raises an Exception indicating that the method is not implemented.

        Raises:
            Exception: Always raises an Exception with the message
            "area() is not implemented".
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that value is a positive integer.

        Args:
            name (str): The name of the value.
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
