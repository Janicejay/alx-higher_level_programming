#!/usr/bin/python3

"""This module contains a class called Square that defines a square."""


class Square:
    """This is the Square class definition."""

    def __init__(self, size=0):
        """__init__ method to initialize the size attribute.
        Args:
            size (int): Size of the square.
        """
        self.__size = size

    def area(self):
        """Calculate the area of the square.
        Returns:
            The area of the square.
