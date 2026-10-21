### Q2b: Universities 
# Write your code below:

def get_average_num_students(filename):

    with open(filename) as reading:

        total = 0
        sch_count = 0

        for line in reading:

            line = line.rstrip('\n')
            columns = line.split('\t')

            total += int(columns[3])
            sch_count += 1

        if sch_count == 0:
            return 0.0

        average = total / sch_count

    return average



