#!/usr/bin/python3

"""This module contains a class called Square that defines a square."""


class Square:
    """This is the Square class definition."""

    def __init__(self, size=0):
        """__init__ method to initialize the size attribute.
        Args:
            size (int): Size of the square.
        """
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
