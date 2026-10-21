### Q5b: Matrix

# Write your code below:

def get_matrix_transpose(filename):

    new_list = []
    final_list = []

    with open(filename) as reading:

        for line in reading:

            line = line.rstrip('\n')
            num_row = line.split(" ")

            new_row = []
            for num in num_row:
                num = float(num)
                new_row.append(num)

            new_list.append(new_row)


    for i in range(len(new_list)):
        transposed = []
        for row in new_list:
            transposed.append(row[i])

        final_list.append(transposed)

    return final_list


