from q2b import generate_loan_report

def run_test_case(tc_num, filename, bank_code, expected_output, expected_type):
    print('*'*40)
    print(f'Test Case {tc_num}: generate_loan_report("{filename}", {bank_code})')
    print()
    print(f'Expected:')
    print(f'{expected_output}')
    result = generate_loan_report(filename,bank_code)
    print(f'Expected return type : {expected_type}')
    print(f'Actual:')
    print(f'{result}')
    print(f"Actual return type   : {type(result)}")
    print()
    print(f'Test Case {tc_num}: {"PASS" if expected_output == result else "FAIL"}')
        

expected_output = [('S**11111', 'DBS000001', 'HOM-LOAN', 100000), ('T**11112', 'DBS000002', 'EDU-LOAN', 125000),('Total Loan Amount', 225000)]
run_test_case(1, 'loandata.txt','DBS', expected_output, type(expected_output))

expected_output = [('S**11111', 'UOB000001', 'CAR-LOAN', 125000),('Total Loan Amount', 125000)]
run_test_case(2, 'loandata.txt','UOB', expected_output, type(expected_output))

expected_output = [('S**11111', 'SCB000001', 'BIZ-LOAN', 100000), ('S**11115', 'SCB000002', 'CAR-LOAN', 100000), ('Total Loan Amount', 200000)]
run_test_case(3, 'loandata.txt','SCB', expected_output, type(expected_output))

expected_output = []
run_test_case(4, 'loandata.txt','ABC', expected_output, type(expected_output))


