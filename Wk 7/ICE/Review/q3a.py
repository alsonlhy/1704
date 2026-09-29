def print_triangle(ch, num_rows):

    for i in range(num_rows):

        formula_ch = 2*i + 1
        formula_space = num_rows - i - 1
        print(' ' * formula_space, end='')
        print(ch * formula_ch)


print_triangle('*', 20)