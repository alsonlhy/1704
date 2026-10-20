### Q1b Reading Files
# Write your code below:


def print_alternate_columns(filename):

    with open(filename) as reading:

        for line in reading:

            line = line.rstrip('\n')
            columns = line.split('&')


            output = ''
            for i in range(0, len(columns),2):

                if i > 0:
                    output += ' & '

                output += columns[i].strip()

            print(output)





