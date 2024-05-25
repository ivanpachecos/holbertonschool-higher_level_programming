#!/usr/bin/python3
"""
This module contains a Rectangle class for representing and manipulating rectangles.
"""


class Rectangle:
    """
    A class used to represent a Rectangle.

    Attributes
    ----------
    width : int
        The width of the rectangle (default is 0).
    height : int
        The height of the rectangle (default is 0).

    Methods
    -------
    __init__(self, width=0, height=0):
        Initializes the Rectangle with a given width and height.
    width(self):
        Gets the width of the rectangle.
    width(self, value):
        Sets the width of the rectangle ensuring it is a non-negative integer.
    height(self):
        Gets the height of the rectangle.
    height(self, value):
        Sets the height of the rectangle ensuring it is a non-negative integer.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes the Rectangle with a given width and height.

        Parameters
        ----------
        width : int, optional
            The width of the rectangle (default is 0).
        height : int, optional
            The height of the rectangle (default is 0).
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Gets the width of the rectangle.

        Returns
        -------
        int
            The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle ensuring it is a non-negative integer.

        Parameters
        ----------
        value : int
            The width to set.

        Raises
        ------
        TypeError
            If the width is not an integer.
        ValueError
            If the width is negative.
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

        Returns
        -------
        int
            The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle ensuring it is a non-negative integer.

        Parameters
        ----------
        value : int
            The height to set.

        Raises
        ------
        TypeError
            If the height is not an integer.
        ValueError
            If the height is negative.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
