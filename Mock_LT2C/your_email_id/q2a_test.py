from q2a import read_trips


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
    run_test("Test Case 1: read_trips('trips-1.txt')", read_trips('trips-1.txt'), [('C001', (2026, 11, 2), 'BUS', 1.19), ('C002', (2026, 11, 2), 'MRT', 1.48), ('C001', (2026, 11, 2), 'MRT', 0.99), ('C001', (2026, 11, 3), 'BUS', 1.19), ('C003', (2026, 11, 3), 'BUS', 2.05)])
    run_test("Test Case 2: read_trips('trips-2.txt')", read_trips('trips-2.txt'), [])
