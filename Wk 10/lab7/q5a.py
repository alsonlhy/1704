### Q5a: Matrix

# Write your code below:

def get_matrix(filename):

    new_list = []

    with open(filename) as reading:

        for line in reading:

            new_line = []

            line = line.rstrip('\n')
            num = line.split(" ")

            for digit in num:
                digit = float(digit)
                new_line.append(digit)

            new_list.append(new_line)


    return new_list



