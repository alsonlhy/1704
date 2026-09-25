def get_matrix_transpose(matrix_list):

    num_rows = len(matrix_list)
    num_cols = len(matrix_list)

    transposed = []

    for cols in range(num_cols):

        new_row = []

        for rows in range(num_rows):
            new_row.append(matrix_list[rows][cols])


        transposed.append(new_row)

            


    return transposed




print(get_matrix_transpose([[1.0, 2.0, 1.5], [2.5, 3.0, 2.0], [4.5, 1.5, 2.5]]))