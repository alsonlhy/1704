# Name: 
# Email ID:

# Write your code below:

def sum_up(file_name):

    sum_file = 0
    
    with open(file_name) as output_file:

        for line in output_file:
            line = line.rstrip('\n')
            sum_file += float(line)

    return sum_file

