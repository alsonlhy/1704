# Name: 
# Email ID:

# Write your code below:

with open('phone_book.txt') as reading:

    for line in reading:
        line = line.rstrip('\n')

        columns = line.split('|')
        phone_num = columns[1]
        if "+65" in phone_num or len(phone_num.lstrip("+()")) == 8:
            print(line)