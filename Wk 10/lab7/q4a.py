with open('transactions.txt') as reading:
    with open('transactions-out-1.txt', 'w') as writing:

        for line in reading:

            line = line.rstrip('\n')
            columns = line.split('\t')

            price = float(columns[2].lstrip('$'))

            if price > 30.0:
                writing.write(line + '\n')
