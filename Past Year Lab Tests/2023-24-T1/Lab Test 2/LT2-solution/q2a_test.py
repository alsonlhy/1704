from q2a import get_special_word_count


def run_test_case(tc_num, filename, expected_output, expected_type):
    print('*'*40)
    print(f'Test Case {tc_num}: get_special_word_count("{filename}")')
    print()
    print(f'Expected: {expected_output}')
    result = get_special_word_count(filename)
    print(f'Actual:   {result}')
    print()
    print(f'Expected return type : {expected_type}')
    print(f"Actual return type   : {type(result)}")
    print()
    print(f'Test Case {tc_num}: {"PASS" if expected_output == result else "FAIL"}')
    
expected_output = 7
run_test_case(1, 'sample1.txt', expected_output, type(expected_output))
