from q2b import get_spending


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
    run_test("Test Case 1: get_spending('trips-1.txt', 'C001')", get_spending('trips-1.txt', 'C001'), (3, 3.37))
    run_test("Test Case 2: get_spending('trips-1.txt', 'C001', 'BUS')", get_spending('trips-1.txt', 'C001', 'BUS'), (2, 2.38))
    run_test("Test Case 3: get_spending('trips-1.txt', 'C001', mode='MRT')", get_spending('trips-1.txt', 'C001', mode='MRT'), (1, 0.99))
    run_test("Test Case 4: get_spending('trips-1.txt', 'C002', 'BUS')", get_spending('trips-1.txt', 'C002', 'BUS'), (0, 0.0))
    run_test("Test Case 5: get_spending('trips-1.txt', 'C009')", get_spending('trips-1.txt', 'C009'), (0, 0.0))
    run_test("Test Case 6: get_spending('trips-2.txt', 'C001')", get_spending('trips-2.txt', 'C001'), (0, 0.0))
