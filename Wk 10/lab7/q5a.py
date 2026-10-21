### Q5a: Matrix

# Write your code below:

def get_matrix(filename):

    new_list = []

    with open(filename) as reading:

        for line in reading:


            line = line.rstrip('\n')
            num_row = line.split(" ")

            new_line = []
            for digit in num_row:
                digit = float(digit)
                new_line.append(digit)

            new_list.append(new_line)


    return new_list



