def print_frame(ch, num_rows, num_cols):


    formula_space = num_cols - 2

    print(ch * num_cols)

    for i in range(num_rows - 2):
        print(ch + ' ' * formula_space + ch)

    print(ch * num_cols)

print_frame('#', 2, 2)