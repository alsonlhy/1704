# Name: 
# Email ID:

# Write your code below:
uniq_names = []
new_list = []

with open('phone_book.txt') as reading:


    for line in reading:

        line = line.rstrip('\n')
        columns = line.split('|')

        name = columns[0]
        phone_num = columns[1]

        if name not in uniq_names:
            uniq_names.append(name)

        new_list.append((name, phone_num))

with open('phone_book_reorganized.txt', 'w') as writing:

    for name in uniq_names:

        writing.write(name + '\n')
        for tup in new_list:
            if name in tup:
                writing.write(tup[1] + '\n')
    
        writing.write('\n')


            

