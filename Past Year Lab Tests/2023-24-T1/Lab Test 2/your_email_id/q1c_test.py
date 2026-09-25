from q1c import get_highest_value

car_info_list = [
    ("BMW 7 Series 730Li Sunroof", 2487, ["$77340", "$73579"]),
    ("Peugeot 308 SW 1.2A PureTech EAT6 Allure", 578, ["$49430", "$9370"]),
    ("Audi A7 Sportback 2.8A FSI Quattro", 2671, ["$56889", "$62923"]),
    ("Mercedes-Benz SLK-Class SLK200K", 3403, ["$5982", "$50320"]),
    ("Audi A4 1.8A TFSI MU", 1978, ["$62000", "$32605"]),
    ("Volkswagen Jetta 1.4A TSI", 3074, ["$28389", "$20546"]),
    ("BMW Z4 sDrive35i", 3285, ["$19830", "$71269"]),
    ("Audi A4 1.8A TFSI V2", 1979, ["$62038", "$32605"]),
    ("Volkswagen Golf 1.4A TSI", 1409, ["$64900", "$5000"]),
]


def run_test_case(tc_num, inputs, expected_output, expected_type):
    print("*" * 40)
    print(f"Test Case {tc_num}: get_highest_value({inputs})")
    print()
    print(f"Expected: {expected_output}")
    result = get_highest_value(inputs)
    print(f"Actual:   {result}")
    print()
    print(f"Expected return type : {expected_type}")
    print(f"Actual return type   : {type(result)}")
    print()
    print(f'Test Case {tc_num}: {"PASS" if expected_output == result else "FAIL"}')


expected_output = "BMW 7 Series 730Li Sunroof"
run_test_case(1, car_info_list, expected_output, type(expected_output))

expected_output = "Audi A7 Sportback 2.8A FSI Quattro"
run_test_case(2, car_info_list[2:], expected_output, type(expected_output))

expected_output = "Audi A4 1.8A TFSI MU"
run_test_case(3, car_info_list[4:], expected_output, type(expected_output))
