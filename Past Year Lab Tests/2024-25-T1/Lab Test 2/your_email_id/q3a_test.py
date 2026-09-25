from q3a import manage_inventory

def check_inventory(inventory):
    """
    This function checks that the inventory:
    1. Is a dictionary
    2. Each dictionary item has the required data type for key and values.
    """
    if not isinstance(inventory, dict):
        return 'Error: Inventory is not a dictionary.\n'
    if not all([isinstance(elem, str) for elem in inventory.keys()]):
        return 'Error: Product names are not all strings.\n'
    if not all([isinstance(elem, list) for elem in inventory.values()]):
        return 'Error: Product info are not all lists.\n'
    if not all([isinstance(elem[0], int) for elem in inventory.values()]):
        return 'Error: Quantity_in_stock are not all integers.\n'
    if not all([isinstance(elem[1], int) for elem in inventory.values()]):
        return 'Error: min_stock are not all integers.\n'
    return ''

def run_test_case(tc_num, filename, expected_output, expected_type):
    print('*'*40)
    print(f'Test Case {tc_num}: manage_inventory("{filename}")')
    print()
    result = manage_inventory(filename)
    print(f'Expected: {expected_output}')
    print(f'Actual  : {result}')
    print(f'Expected return type : {expected_type}')
    print(f"Actual return type   : {type(result)}")
    print()
    error_message = check_inventory(result)
    if not error_message:
        print(f'Test Case {tc_num}: {"PASSED" if expected_output == result else "FAILED"}')
    else:
        print(error_message)
        print(f'Test Case {tc_num}: FAILED')
    print()

expected_output = {'Laptop': [25, 15], 'Phone': [50, 15], 'Chair': [100, 8], 'Sofa': [10, 8], 'TV': [30, 8], 'Table': [20, 8], 'Headphones': [60, 3], 'Refrigerator': [8, 3], 'Microwave': [15, 3], 'Lamp': [40, 3]}
run_test_case(1, "inventory1.txt", expected_output, type(expected_output))

expected_output = {'Apple': [100, 15], 'Tomato': [50, 8], 'Orange': [150, 8], 'Potato': [70, 3], 'Cucumber': [40, 3], 'Coca': [30, 3]}
run_test_case(2, "inventory2.txt", expected_output, type(expected_output))

expected_output = {}
run_test_case(3, "inventory3.txt", expected_output, type(expected_output))