# Name:
# Email ID:


def generate_loan_report(filename, bank_code):

    summary = []

    with open (filename) as reading:

        for line in reading:
            line = line.rstrip("\n")
            value = line.split(",")

            nric = value[0]
            branch = value[1]
            loan_type = value[2]
            amt = int(value[3].lstrip("$"))

            if bank_code in branch:
                summary.append((nric, branch, loan_type, amt))

    if bank_code not in branch:
        return []
    
    total_amt = 0
    for tup in summary:

        total_amt += tup[3]

    summary.append(('Total Loan Amount', total_amt))
                
    return summary
        
        

