#!/usr/bin/python3
""" appends a string """


def append_write(filename="", text=""):
    """ function that appends a string at the end of a text file (UTF8)
    and returns the number of characters added """
    with open(filename, mode="a", encoding="UTF8") as myFile:
        return(myFile.write(text))
