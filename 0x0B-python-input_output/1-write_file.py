#!/usr/bin/python3
""" Writes a string to a file """


def write_file(filename="", text=""):
    """ function that writes a string to a text file
    and returns the number of characters written """
    with open(filename, mode="w", encoding="UTF8") as myFile:
        return(myFile.write(text))
