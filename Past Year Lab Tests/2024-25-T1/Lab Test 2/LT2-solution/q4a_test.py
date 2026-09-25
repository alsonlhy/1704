from q4a import get_invalid_transactions

def run_test_case(tc_num, filename, expected_output, expected_type):
        print('*'*40)
        print(f'Test Case {tc_num}: get_invalid_transactions("{filename}")')
        print()
        print(f'Expected: {expected_output}')
        result = get_invalid_transactions(filename)
        print(f'Actual:   {result}')
        print()
        print(f'Expected return type : {expected_type}')
        print(f"Actual return type   : {type(result)}")
        print()
        print(f'Test Case {tc_num}: {"PASSED" if expected_output == result else "FAILED"}')

    
expected_output = ['TX008', 'TX013', 'TX014', 'TX015']
run_test_case(1, 'transactions_1.txt', expected_output, type(expected_output))

expected_output = []
run_test_case(2, 'transactions_2.txt', expected_output, type(expected_output))
