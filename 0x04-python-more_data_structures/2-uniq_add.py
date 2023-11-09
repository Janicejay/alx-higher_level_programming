#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    unique_integers = set()

    for idx in range(len(my_list)):
        if my_list[idx] not in unique_integers:
            unique_integers.add(my_list[idx])
            result += my_list[idx]

    return result
