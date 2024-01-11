#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Create a new matrix to store squared values
    result_matrix = []

    # Iterate over each row in the original matrix
    for row in matrix:
        # Create a new row for the result matrix
        result_row = []
        # Iterate over each element in the row and append its square to the result row
        for element in row:
            result_row.append(element ** 2)
        # Append the result row to the result matrix
        result_matrix.append(result_row)

    return result_matrix
