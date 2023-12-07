#!/usr/bin/python3
""" script that adds all arguments
"""


if __name__ == "__main__":
    import json
    from sys import argv

    save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
    load_from_json_file = \
        __import__("6-load_from_json_file").load_from_json_file

    with open("add_item.json", "a+", encoding="utf-8") as file:
        if file.tell() == 0:
            json.dump([], file)
    file_input = load_from_json_file("add_item.json")

    if len(argv) > 1:
        file_input.extend(argv[1:])

    save_to_json_file(file_input, "add_item.json")
