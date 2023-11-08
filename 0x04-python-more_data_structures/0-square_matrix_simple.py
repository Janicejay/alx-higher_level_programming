#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    squared_matrix = []

    for row_idx in range(len(matrix)):
        squared_row = []

        for col_idx in range(len(matrix[row_idx])):
            element = matrix[row_idx][col_idx]
            squared_element = element ** 2
            squared_row.append(squared_element)

        squared_matrix.append(squared_row)

    return squared_matrix
