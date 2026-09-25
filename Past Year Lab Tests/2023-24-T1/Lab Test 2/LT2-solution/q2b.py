# Name:
# Email ID:


def generate_loan_report(filename, bank_code):
    # Replace the code below with your implementation.
    
    bank_dict = {}
    with open(filename, 'r') as my_file:
        for line in my_file:
            line = line.rstrip('\n')
            columns = line.split(',')
            cust_nirc = columns[0]
            cur_bank_code = columns[1][0:3]
            bank_id = columns[1]
            loan_type = columns[2]
            amount = int(columns[3][1:])
            if cur_bank_code not in bank_dict:
                bank_dict[cur_bank_code] = [ (cust_nirc, bank_id, loan_type, amount) ]
            else:
                tup_list = bank_dict[cur_bank_code]
                tup_list.append( (cust_nirc, bank_id, loan_type, amount) )
                
    bank_tup_list = []
    tot_amount = 0
    
    if bank_code in bank_dict:
        bank_tup_list = bank_dict[bank_code]
        for tup in bank_tup_list:
            tot_amount += tup[3]

        bank_tup_list.append( ('Total Loan Amount', tot_amount) )
    return bank_tup_list
        
        

