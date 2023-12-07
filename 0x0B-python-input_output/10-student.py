!/usr/bin/python3
""" Student to JSON with filter """


class Student:
    """ class Student """

    def __init__(self, first_name, last_name, age):
        """ defines a student by
        first name, last name and age"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Public method that retrieves a dictionary
        representation of a Student """
        new = {}

        if attrs is None:
            return self.__dict__

        for attr in attrs:
            if attr in self.__dict__.keys():
                new[attr] = self.__dict__[attr]

        return
