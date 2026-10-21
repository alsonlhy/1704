## Q1 Reading Files
# Write your code below:
##############################

def print_alternate_lines(filename):

    with open(filename) as reading:

        line_num = 0
        for line in reading:
            line = line.rstrip('\n')
            if line_num % 2 ==0:
                print(line)
            line_num += 1
            




