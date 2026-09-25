from q1b import alternate_and_reverse

strings_inputs = [
    ('', ''),
    ('', 'abcde'),
    ('xyz123', ''),
    ('abc', 'def'),
    ('abcde', '123'),
    ('xyz', '78901'),
]


def run_test_case(tc_num, strings_inputs, expected_output, expected_type):
    print("*" * 40)
    print(f"Test Case {tc_num}: alternate_and_reverse('{strings_inputs[tc_num-1][0]}', '{strings_inputs[tc_num-1][1]}')")
    print()
    print(f"Expected: {expected_output}")
    result = alternate_and_reverse(strings_inputs[tc_num-1][0], strings_inputs[tc_num-1][1])
    print(f"Actual:   {result}")
    print()
    print(f"Expected return type : {expected_type}")
    print(f"Actual return type   : {type(result)}")
    print()
    print(f'Test Case {tc_num}: {"PASSED" if expected_type is type(result) and expected_output == result else "FAILED"}')


expected_output = ''
run_test_case(1, strings_inputs, expected_output, type(expected_output))

expected_output = 'edcba'
run_test_case(2, strings_inputs, expected_output, type(expected_output))

expected_output = '321zyx'
run_test_case(3, strings_inputs, expected_output, type(expected_output))

expected_output = 'adbecf'
run_test_case(4, strings_inputs, expected_output, type(expected_output))

expected_output = 'a1b2c3ed'
run_test_case(5, strings_inputs, expected_output, type(expected_output))

expected_output = 'x7y8z910'
run_test_case(6, strings_inputs, expected_output, type(expected_output))