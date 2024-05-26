#!/usr/bin/python3
"""
Calculate the area of a square
"""


class Square:
    """
    Defines a square
    """

    def __init__(self, size=0):
        """
        Initialize a new Square instance.

        Parameters:
        size (int): The size of one side of the square (default is 0).

        Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
        int: The area of the square.
        """
        return self.__size * self.__size

    @property
    def size(self):
        """
        Get the size of the square.

        Returns:
        int: The size of one side of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Parameters:
        value (int): The new size of one side of the square.

        Raises:
        TypeError: If value is not an integer.
        ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value
