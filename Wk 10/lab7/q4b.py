with open('transactions.txt') as reading:
    with open('transactions-output-2.txt', 'w') as writing:

        uniq_list = []
        edited_list = []

        for line in reading:


            line = line.rstrip('\n')
            columns = line.split('\t')
            price = float(columns[2].lstrip('$'))
            month_yr = columns[0][3:]
            edited_list.append((month_yr, columns[1], price))

            if month_yr not in uniq_list:
                uniq_list.append(month_yr)

        for uniq in uniq_list:

            total = 0
            details = ""

            for tup in edited_list:
                if uniq == tup[0]:
                    total += tup[2]
                    details += "    " + tup[1] + "\t" + "$" + f"{tup[2]:.2f}" + "\n"

            writing.write(f"{uniq}: total transaction amount is ${total:.2f}\n")
            writing.write(details + "\n")


            
