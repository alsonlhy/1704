from q1a import get_good_stalls


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
    stalls = [('Ah Huat Duck Rice', 4.6, 320), ('Uncle Lim Char Kway Teow', 4.8, 95), ('Mei Mei Chicken Rice', 4.4, 1500), ('Bala Satay', 4.6, 100)]
    copy = list(stalls)
    run_test('Test Case 1: get_good_stalls(stalls, 4.5, 100)', get_good_stalls(stalls, 4.5, 100), ['Ah Huat Duck Rice', 'Bala Satay'])
    run_test('Test Case 2: get_good_stalls(stalls, 4.4, 95)', get_good_stalls(stalls, 4.4, 95), ['Ah Huat Duck Rice', 'Uncle Lim Char Kway Teow', 'Mei Mei Chicken Rice', 'Bala Satay'])
    run_test('Test Case 3: get_good_stalls(stalls, 4.9, 0)', get_good_stalls(stalls, 4.9, 0), [])
    run_test('Test Case 4: get_good_stalls([], 4.0, 10)', get_good_stalls([], 4.0, 10), None)
    run_test('Test Case 5: stalls == copy', stalls == copy, True)
