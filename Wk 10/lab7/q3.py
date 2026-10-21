with open ('temperatures.txt') as reading:

    for line in reading:
        line = line.rstrip('\n')
        columns = line.split('\t')
        name = columns[0]

        min_temp = float(columns[1])
        max_temp = float(columns[1])
        max_temp = 0

        for i in range(1,len(columns)):

            if float(columns[i]) < min_temp:
                min_temp = float(columns[i])

            if float(columns[i]) > max_temp:
                max_temp = float(columns[i])

        print(f"{name}: {min_temp}, {max_temp}")