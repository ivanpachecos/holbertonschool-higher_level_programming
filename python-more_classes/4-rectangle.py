#!/usr/bin/python3
"""
This module contains a Rectangle class for representing and manipulating
rectangles.
"""


class Rectangle:
    """
    A class used to represent a Rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes the Rectangle with a given width and height.
        """
        self.width = width
        self.height = height

    def __repr__(self):
        """
        Obtain the chain representation
        """
        return f"Rectangle{self.width, self.height}"

    def __str__(self):
        """
        Print '#' with area and premeter
        """
        rect = []
        if self.width == 0 or self.height == 0:
            return ""
        for _ in range(self.height):
            rect.append("#" * self.width)
        return "\n".join(rect)

    def area(self):
        """
        Calculate the mul of two values
        """
        return (self.width * self.height)

    def perimeter(self):
        """
        Calculate the sum of its perimeter
        """
        if self.height == 0 or self.width == 0:
            return (0)
        return (self.width + self.width + self.height + self.height)

    @property
    def width(self):
        """
        Gets the width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle ensuring it is a non-negative integer.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Gets the height of the rectangle.
        -------
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle ensuring it is a non-negative integer.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
