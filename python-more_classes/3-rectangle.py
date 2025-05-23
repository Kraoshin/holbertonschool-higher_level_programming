#!/usr/bin/python3
"""
This module defines a class Rectangle with width and height attributes,
and methods to calculate area, perimeter, and represent the rectangle
as a string of '#' characters.
"""


class Rectangle:
    """
    This class defines a rectangle by its width and height.

    Attributes:
        __width (int): The width of the rectangle (private).
        __height (int): The height of the rectangle (private).

    Methods:
        __init__(self, width=0, height=0): Initializes the rectangle.
        width(self): Retrieves the width of the rectangle.
        width(self, value): Sets the width of the rectangle.
        height(self): Retrieves the height of the rectangle.
        height(self, value): Sets the height of the rectangle.
        area(self): Returns the area of the rectangle.
        perimeter(self): Returns the perimeter of the rectangle.
        __str__(self): Returns a string representation of the rectangle
            using the character '#'.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes the rectangle with private instance attributes
        width and height.

        Args:
            width (int): The width of the rectangle. Defaults to 0.
            height (int): The height of the rectangle. Defaults to 0.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle.

        Args:
            value (int): The width of the rectangle.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.

        Args:
            value (int): The height of the rectangle.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Returns the current rectangle area.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Returns the current rectangle perimeter.

        Returns:
            int: The perimeter of the rectangle, or 0 if width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns a string representation of the rectangle using '#'.
        If width or height is 0, returns an empty string.

        Returns:
            str: The string representation of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle_str = ""
        for _ in range(self.__height):
            rectangle_str += "#" * self.__width
            if _ != self.__height - 1:
                rectangle_str += "\n"
        return rectangle_str
