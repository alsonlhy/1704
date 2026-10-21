### Q2a: Universities 
# Write your code below:

def get_universities_founded_before(filename, year):

    with open(filename) as reading:

        uni_list = []

        for line in reading:
            line = line.rstrip('\n')
            columns = line.split('\t')

            uni_name = columns[0]
            founding_yr = int(columns[2])
            if founding_yr < year:
                uni_list.append(uni_name)

    return uni_list

