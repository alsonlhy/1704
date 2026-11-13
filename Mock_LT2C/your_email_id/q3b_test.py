from q3b import get_rejected


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
    run_test("Test Case 1: get_rejected('wallet-1.txt')", get_rejected('wallet-1.txt'), {'C002': [(3, 1.48)], 'C001': [(5, 9.0)], 'C003': [(8, 0.5)]})
    run_test("Test Case 2: get_rejected('wallet-2.txt')", get_rejected('wallet-2.txt'), {})
    run_test("Test Case 3: get_rejected('wallet-3.txt')", get_rejected('wallet-3.txt'), {})
