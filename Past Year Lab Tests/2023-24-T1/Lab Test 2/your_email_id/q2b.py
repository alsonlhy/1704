# Name:
# Email ID:


def generate_loan_report(filename, bank_code):

    summary = []
    total_amt = 0

    with open (filename) as reading:

        for line in reading:
            line = line.rstrip("\n")
            value = line.split(",")

            nric = value[0]
            branch = value[1]
            loan_type = value[2]
            amt = int(value[3].lstrip("$"))

            if branch[:3] == bank_code:
                summary.append((nric, branch, loan_type, amt))
                total_amt += amt

    if len(summary) > 0:
        summary.append(('Total Loan Amount', total_amt))
                
    return summary
        
        

