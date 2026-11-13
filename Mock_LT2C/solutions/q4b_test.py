from q4b import get_rooms_needed


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
    run_test("Test Case 1: get_rooms_needed('bookings-1.txt')", get_rooms_needed('bookings-1.txt'), (5, '10:45'))
    run_test("Test Case 2: get_rooms_needed('bookings-2.txt')", get_rooms_needed('bookings-2.txt'), (0, None))
    run_test("Test Case 3: get_rooms_needed('bookings-3.txt')", get_rooms_needed('bookings-3.txt'), (2, '14:30'))
