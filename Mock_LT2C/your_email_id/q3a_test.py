from q3a import get_balances


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
    run_test("Test Case 1: get_balances('wallet-1.txt')", get_balances('wallet-1.txt'), {'C001': 0.0, 'C002': 3.52, 'C003': 0.0})
    run_test("Test Case 2: get_balances('wallet-2.txt')", get_balances('wallet-2.txt'), {'A1': 0.0})
    run_test("Test Case 3: get_balances('wallet-3.txt')", get_balances('wallet-3.txt'), {})
