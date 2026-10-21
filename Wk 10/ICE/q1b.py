# Name: 
# Email ID:

# Write your code below:

def create_num_file(output_file, n):

    with open(output_file, 'w') as input_file:

        for i in range(0,n+1,2):
            input_file.write(str(i) + '\n')
    
