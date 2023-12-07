#!/usr/bin/python3
""" Pascal's Triangle """


def pascal_triangle(n):
    """ function that returns a list of
    lists of integers representing the Pascal triangle """
    pasc_list = []

    for i in range(n):
        pasc_list.append([])
        pasc_list[i].append(1)
        for j in range(1, i):
            pasc_list[i].append(pasc_list[i - 1][j - 1] + pasc_list[i - 1][j])
        if (i != 0):
            pasc_list[i].append(1)
    return
