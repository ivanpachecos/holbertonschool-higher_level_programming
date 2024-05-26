#!/usr/bin/python3
"""
Calculate the area of a square
"""


class Square:
    """
    Defines a square
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a new Square instance.

        Parameters:
        size (int): The size of one side of the square (default is 0).
        position (tuple): The position of the square (default is (0, 0)).

        Raises:
        TypeError: If size is not an integer or position is not a tuple
        of 2 positive integers.
        ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
        self.position = position

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

    @property
    def position(self):
        """
        Get the position of the square.

        Returns:
        tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the square.

        Parameters:
        value (tuple): The new position of the square.

        Raises:
        TypeError: If position is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
            not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def my_print(self):
        """
        Print the square with the character "#".

        If the size is 0, print an empty line.
        """
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__position[1]):
                print("")
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
