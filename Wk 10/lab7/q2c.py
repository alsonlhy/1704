### Q2c: Universities 
# Write your code below:

def search_with_keyword(filename, keyword):

    with open(filename) as reading:

        acro_list = []
        keyword = keyword.lower()

        for line in reading:
            line = line.rstrip('\n')
            columns = line.split('\t')

            if keyword in line.lower():
                acro_list.append(columns[1])


    return acro_list
