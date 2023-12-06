#!/usr/bin/python3
""" class MyList """


class MyList(list):
    """ class MyList that inherits from list """

    def __init__(self):

        super().__init__()

    def print_sorted(self):
        """ prints the list in ascending order """
        sort_list = self.copy()
        sort_list.sort()
        print(sort_list)
