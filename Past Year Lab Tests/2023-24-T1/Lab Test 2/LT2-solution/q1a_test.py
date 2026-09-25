from q1a import compute_coe_rebate

cars_info = [
    ("Peugeot 308 SW 1.2A PureTech EAT6 Allure", 578, ["$49430", "$9370"]),
    ("Volkswagen Jetta 1.4A TSI", 3074, ["$28389", "$20546"]),
    ("Mercedes-Benz SLK-Class SLK200K", 3403, ["$5982", "$50320"]),
    ("BMW Z4 sDrive35i", 3285, ["$19833", "$71269"]),
]


def run_test_case(tc_num, expected_output, expected_type):
    print("*" * 40)
    print(f"Test Case {tc_num}: compute_coe_rebate({cars_info[tc_num-1]})")
    print()
    print(f"Expected: {expected_output}")
    result = compute_coe_rebate(cars_info[tc_num - 1])
    print(f"Actual:   {result}")
    print()
    print(f"Expected return type : {expected_type}")
    print(f"Actual return type   : {type(result)}")
    print()
    print(f'Test Case {tc_num}: {"PASS" if expected_output == result else "FAIL"}')
    

expected_output = 41602
run_test_case(1, expected_output, type(expected_output))

expected_output = 4480
run_test_case(2, expected_output, type(expected_output))

expected_output = 404
run_test_case(3, expected_output, type(expected_output))

expected_output = 1983
run_test_case(4, expected_output, type(expected_output))
