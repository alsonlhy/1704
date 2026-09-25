from q4 import calculate_actual_delays
def run_test_case(tc_num, list_cars, traffic_lights, expected_output, expected_type):
        print('*'*40)
        print(f'Test Case {tc_num}: calculate_actual_delays({list_cars}, {traffic_lights})')
        print()
        print(f'Expected: {expected_output}')
        result = calculate_actual_delays(list_cars, traffic_lights)
        print(f'Actual:   {result}')
        print()
        print(f'Expected return type : {expected_type}')
        print(f"Actual return type   : {type(result)}")
        print()
        print(f'Test Case {tc_num}: {"PASS" if expected_output == result else "FAIL"}')

    
expected_output = ([[(1, 2), (2, 5), (3, 7), (4, 10)]], 1)
run_test_case(1, [[(1, 2), (2, 3), (3, 2), (4, 3)]], (10, 5), expected_output, type(expected_output))

expected_output = ([[(1, 5), (2, 10), (3, 20), (4, 24)]], 2)
run_test_case(2, [[(1, 5), (2, 5), (3, 5), (4, 4)]], (10, 5), expected_output, type(expected_output))

expected_output = ([[(1, 2), (2, 4), (3, 12)], [(4, 4), (5, 10), (6, 40), (7, 51)], [(8, 15), (9, 26)]], 3)
run_test_case(3, [[(1, 2), (2, 2), (3, 8)], [(4, 4), (5, 6), (6, 15), (7, 1)], [(8, 15), (9, 1)]], (15, 10), expected_output, type(expected_output))