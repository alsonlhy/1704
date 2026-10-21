# Name: 
# Email ID:

# Write your code below:

def check_same_author(file_name):

    author_name = []
    check = 0

    with open(file_name) as reading:
        for line in reading:

            line = line.rstrip('\n')
            columns = line.split('\t')
            author = columns[1]
            author_name.append(author)

    for name in author_name:
        if name == author_name[0]:
            check = 1
        else: 
            check = 0

    if check == 1:
        return True
    else: 
        return False


# try unique author method, if author not in [], then append in. if len[] >1 then false
