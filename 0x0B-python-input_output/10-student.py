#!/usr/bin/python3
"""Student that defines a student"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns the dictionary representation of a student"""

        if attrs is None:
            return self.__dict__
        new_dict = {}
        for a in attrs:
            if a in self.__dict__:
                new_dict[a] = self.__dict__[a]
        return new_dict
