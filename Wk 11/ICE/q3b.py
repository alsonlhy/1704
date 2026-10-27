# Name: 
# Email ID: 

def read_into_dict(filename):

    new_dict = {}

    with open(filename) as reading:

        for line in reading:
            line = line.rstrip("\n")
            column = line.split("\t")

            new_dict[column[0]] = column[1]

    return new_dict




