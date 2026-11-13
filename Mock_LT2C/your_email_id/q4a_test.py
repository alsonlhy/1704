from q4a import get_clashes


def run_test(label, result, expected):
    print(label)
    print('-' * 40)
    print('Expected:', repr(expected))
    print('Actual:  ', repr(result))
    print('Expected type:', type(expected))
    print('Actual type:  ', type(result))
    print('Is the returned value as expected?', result == expected and type(result) == type(expected))
    print()

if __name__ == '__main__':
    run_test("Test Case 1: get_clashes('bookings-1.txt')", get_clashes('bookings-1.txt'), [('B01', 'B04'), ('B02', 'B04'), ('B03', 'B06'), ('B05', 'B06')])
    run_test("Test Case 2: get_clashes('bookings-2.txt')", get_clashes('bookings-2.txt'), [])
    run_test("Test Case 3: get_clashes('bookings-3.txt')", get_clashes('bookings-3.txt'), [])
