#!/usr/bin/python3
""" Writes Object to a file """


import json


def save_to_json_file(my_obj, filename):
    """ function that writes an Object to a
    text file, using a JSON representation """

    with open(filename, mode="w", encoding="UTF8") as myfile:
        myfile.write(json.dumps(my_obj))
