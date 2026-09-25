from q2b import get_swim_report

def run_test_case(tc_num, filename, swimmer_name, event_name, expected_output, expected_type):
    print('*'*40)
    print(f'Test Case {tc_num}: get_swim_report("{filename}", "{swimmer_name}", "{event_name}")')
    print()
    result = get_swim_report(filename, swimmer_name, event_name)
    print(f'Expected: {expected_output}')
    print(f'Actual  : {result}')
    print(f'Expected return type : {expected_type}')
    print(f"Actual return type   : {type(result)}")
    print()
    print(f'Test Case {tc_num}: {"PASSED" if expected_output == result else "FAILED"}')
    print()

expected_output = (2, 62)
run_test_case(1, "swimtimes-sample.csv", "Michael Phelps", "50m doggy paddle", expected_output, type(expected_output))

expected_output = (1, 42)
run_test_case(2, "swimtimes-sample.csv", "Shanti Pereira", "50m backstroke", expected_output, type(expected_output))

expected_output = (0, 0)
run_test_case(3, "swimtimes-sample.csv", "Shanti Pereira", "50m doggy paddle", expected_output, type(expected_output))

expected_output = (2, 42)
run_test_case(4, "swimtimes-sample2.csv", "Joseph Schooling", "50m butterfly", expected_output, type(expected_output))

expected_output = (1, 37)
run_test_case(5, "swimtimes-sample2.csv", "Penny Oleksiak", "50m freestyle", expected_output, type(expected_output))

