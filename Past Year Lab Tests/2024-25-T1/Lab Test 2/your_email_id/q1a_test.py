from q1a import sum_values_by_weights

shipments_info = [
    [(9.9, 4), (11.25, 5), (10.0, 10), (18.70, 100)],
    [(13.0, 4), (21.03, 8), (10.01, 50), (19.99, 29)],
    [],
]


def run_test_case(tc_num, shipments_info, expected_output, expected_type):
    print("*" * 40)
    print(f"Test Case {tc_num}: sum_values_by_weights({shipments_info[tc_num-1]})")
    print()
    print(f"Expected: {expected_output}")
    result = sum_values_by_weights(shipments_info[tc_num-1])
    print(f"Actual:   {result}")
    print()
    print(f"Expected return type : {expected_type}")
    print(f"Actual return type   : {type(result)}")
    print()
    print(f'Test Case {tc_num}: {"PASSED" if expected_type is type(result) and expected_output == result else "FAILED"}')


expected_output = 14
run_test_case(1, shipments_info, expected_output, type(expected_output))

expected_output = 0
run_test_case(2, shipments_info, expected_output, type(expected_output))

expected_output = None
run_test_case(3, shipments_info, expected_output, type(expected_output))
