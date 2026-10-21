# Name: 
# Email ID:

# Write your code below:

def get_books_cheaper_than(input_file, price_limit, output_file):

    with open(input_file) as reading:
        with open(output_file,'w') as writing:

            for line in reading:
                columns = line.split('\t')

                name = columns[0]
                price = float(columns[2].lstrip('$'))

                if price < price_limit:
                    writing.write(line + '\n')
