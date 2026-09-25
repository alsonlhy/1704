from q3b import process_orders

def check(order_res):
    """
    This function checks that the order processing result:
    1. Is a dictionary
    2. Each dictionary item has the required data type for key and values.
    """
    if not isinstance(order_res, dict):
        return 'Error: Order processing result is not a dictionary.\n'
    if not all([isinstance(elem, str) for elem in order_res.keys()]):
        return 'Error: Dictionary keys are not customers names.\n'
    if not all([isinstance(elem, list) for elem in order_res.values()]):
        return 'Error: Dictionary values are not lists for all customers.\n'

    for elem in order_res.values():
        if not all([isinstance(e, tuple) for e in elem]):
            return 'Error: Dictionary values not all consist of tuples.\n'
        if not all([isinstance(e[2], int) and isinstance(e[3], int) for e in elem]):
            return 'Error: Quantities are not all integers.\n'
            
    return ''

def run_test_case(tc_num, filename, orders, expected_output, expected_type):
    print('*'*40)
    print(f'Test Case {tc_num}: process_orders("{filename}", {orders})')
    print()
    result = process_orders(filename, orders)
    print(f'Expected: {expected_output}')
    print(f'Actual  : {result}')
    print(f'Expected return type : {expected_type}')
    print(f"Actual return type   : {type(result)}")
    print()
    error_message = check(result)
    if not error_message:
        print(f'Test Case {tc_num}: {"PASSED" if expected_output == result else "FAILED"}')
    else:
        print(error_message)
        print(f'Test Case {tc_num}: FAILED')
    print()

orders1 = [(1, 'Alice', 'Laptop', 30), (2, 'Bob', 'Phone', 50), (3, 'Carol', 'Chair', 10), (4, 'David', 'TV', 30), (5, 'Alice', 'Headphones', 40), (6, 'Bob', 'Sofa', 10), (7, 'Carol', 'Microwave', 20), (8, 'David', 'Table', 10)]
expected_output = {'Alice': [(1, 'Laptop', 30, 25), (5, 'Headphones', 40, 40)], 'Bob': [(2, 'Phone', 50, 50), (6, 'Sofa', 10, 10)], 'Carol': [(3, 'Chair', 10, 10), (7, 'Microwave', 20, 15)], 'David': [(4, 'TV', 30, 30), (8, 'Table', 10, 10)]}
run_test_case(1, "inventory1.txt", orders1, expected_output, type(expected_output))

orders2 = [(1, 'Alice', 'Apple', 80), (2, 'Bob', 'Apple', 50), (3, 'Carol', 'Tomato', 60), (4, 'David', 'Orange', 130), (5, 'Alice', 'Orange', 40), (6, 'Bob', 'Coca', 100), (7, 'Carol', 'Potato', 120), (8, 'David', 'Tomato', 40)]
expected_output = {'Alice': [(1, 'Apple', 80, 80), (5, 'Orange', 40, 20)], 'Bob': [(2, 'Apple', 50, 20), (6, 'Coca', 100, 30)], 'Carol': [(3, 'Tomato', 60, 50), (7, 'Potato', 120, 70)], 'David': [(4, 'Orange', 130, 130), (8, 'Tomato', 40, 0)]}
run_test_case(2, "inventory2.txt", orders2, expected_output, type(expected_output))

orders3 = [(1, 'Alice', 'Apple', 80), (2, 'Bob', 'Apple', 50), (3, 'Carol', 'Tomato', 60), (4, 'David', 'Orange', 130), (5, 'Alice', 'Orange', 40), (6, 'Bob', 'Coca', 100), (7, 'Carol', 'Potato', 120), (8, 'David', 'Tomato', 40)]
expected_output = {'Alice': [(1, 'Apple', 80, 0), (5, 'Orange', 40, 0)], 'Bob': [(2, 'Apple', 50, 0), (6, 'Coca', 100, 0)], 'Carol': [(3, 'Tomato', 60, 0), (7, 'Potato', 120, 0)], 'David': [(4, 'Orange', 130, 0), (8, 'Tomato', 40, 0)]}
run_test_case(3, "inventory3.txt", orders3, expected_output, type(expected_output))

orders4 = []
expected_output = {}
run_test_case(4, "inventory3.txt", orders4, expected_output, type(expected_output))