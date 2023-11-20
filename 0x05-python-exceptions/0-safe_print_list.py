#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    element = 0
    for i in my_list:
        try:
            if element < x:
                print(i, end=' ')
                element += 1
        except IndexError:
            break
    print('')
    return element
