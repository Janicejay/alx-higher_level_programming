#!/usr/bin/python3
""" appends a string """


def append_write(filename="", text=""):
    """ function that appends a string at the end of a text file (UTF8)
    and returns the number of characters added """
    if not filename:
        return 0
    with open(filename, mode="a", encoding="UTF-8") as myFile:
        return myFile.write(text)
