from q2a import get_entry_count

def run_test_case(tc_num, filename, swimmer, expected_output, expected_type):
    print('*'*40)
    if swimmer:
        print(f'Test Case {tc_num}: get_entry_count("{filename}", "{swimmer}")')
    else:
        print(f'Test Case {tc_num}: get_entry_count("{filename}")')
    print()
    print(f'Expected: {expected_output}')
    if swimmer:
        result = get_entry_count(filename, swimmer)
    else:
        result = get_entry_count(filename)
    print(f'Actual  : {result}')
    print()
    print(f'Expected return type : {expected_type}')
    print(f"Actual return type   : {type(result)}")
    print()
    print(f'Test Case {tc_num}: {"PASSED" if expected_output == result else "FAILED"}')
    
expected_output = 4
run_test_case(1, 'swimtimes-sample.csv', None, expected_output, type(expected_output))

expected_output = 2
run_test_case(2, 'swimtimes-sample.csv', "Shanti Pereira", expected_output, type(expected_output))

expected_output = 20
run_test_case(3, 'swimtimes-sample2.csv', None, expected_output, type(expected_output))

expected_output = 4
run_test_case(4, 'swimtimes-sample2.csv', "Joseph Schooling", expected_output, type(expected_output))
