def read_recycling_data(filename):

    records = []

    with open(filename) as reading:
        reading.readline()

        for line in reading:

            line = line.rstrip('\n')
            columns = line.split('%')

            site = columns[0]
            paper = int(columns[1])
            plastic = int(columns[2])

            records.append((site, paper, plastic))

    return records


def find_major_collection_sites(filename, min_weight):
    new_records = []

    read = read_recycling_data()

    for tup in read:
        if tup[1] >= min_weight or tup[2] >= min_weight:

            site = tup[0]

            if tup[1] > tup[2]:
                new_mat = 'Paper'
            else:
                new_mat = 'Plastic'

            total_weight = tup[1] + tup[2]
            new_records.append((site, new_mat, total_weight))

    return new_records


            