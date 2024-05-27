#!/usr/bin/python3
"""
This module defines a class MyList that inherits from the built-in list class.
The MyList class includes a method to print the list elements in sorted order.
"""


class MyList(list):
    """
    MyList is a subclass of the built-in list class.
    It provides an additional method to print the list in ascending sorted
    order.
    """

    def print_sorted(self):
        """
        Prints the elements of the list in ascending sorted order.

        This method does not modify the original list; it creates a sorted
        copy
        of the list and prints that sorted copy.
        """
        sorted_order = sorted(self)  # Create a sorted copy of the list
        print(sorted_order)  # Print the sorted copy
