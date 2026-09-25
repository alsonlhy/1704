from q4b import get_coins
def run_test_case(tc_num, filename, address, target, expected_output, expected_type):
        print('*'*40)
        print(f'Test Case {tc_num}: get_coins("{filename}", "{address}", {target})')
        print()
        print(f'Expected: {expected_output}')
        result = get_coins(filename, address, target)
        if result is not None:
                result = sorted([tuple(sorted(tup)) for tup in result])
        print(f'Actual:   {result}')
        print()
        print(f'Expected return type : {expected_type}')
        print(f"Actual return type   : {type(result)}")
        print()
        print(f'Test Case {tc_num}: {"PASSED" if expected_output == result else "FAILED"}')

    
expected_output = [(2, 2, 2, 4), (2, 2, 6), (2, 4, 4), (2, 8), (4, 6)]
run_test_case(1, 'transactions_2.txt', 'MinerA', 10, expected_output, type(expected_output))

expected_output = [(2, 2, 2, 4, 4), (2, 2, 2, 8), (2, 2, 4, 6), (2, 4, 8), (4, 4, 6), (6, 8)]
run_test_case(2, 'transactions_2.txt', 'MinerA', 13, expected_output, type(expected_output))

expected_output = []
run_test_case(3, 'transactions_2.txt', 'MinerB', 5, expected_output, type(expected_output))
