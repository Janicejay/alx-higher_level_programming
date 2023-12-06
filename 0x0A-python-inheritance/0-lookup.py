#!/usr/bin/python3
"""Returns available attributes
and methods of an object
"""


def lookup(obj):
    """Returns a list of available attributes """

    return dir(obj)
