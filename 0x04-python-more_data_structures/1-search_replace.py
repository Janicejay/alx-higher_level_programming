#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for search_idx in range(len(my_list)):
        if my_list[search_idx] == search:
            new_list.append(replace)
            continue
        new_list.append(my_list[search_idx])

    return new_list

