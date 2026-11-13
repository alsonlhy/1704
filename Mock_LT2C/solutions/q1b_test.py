from q1b import get_initials


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
    run_test("Test Case 1: get_initials('tan ah kow;lim bee hoon; ong')", get_initials('tan ah kow;lim bee hoon; ong'), 'TAK-LBH-O')
    run_test("Test Case 2: get_initials('  mary   ann  ')", get_initials('  mary   ann  '), 'MA')
    run_test("Test Case 3: get_initials('Siti Nurhaliza;a;;b')", get_initials('Siti Nurhaliza;a;;b'), 'SN-A-B')
    run_test("Test Case 4: get_initials('')", get_initials(''), '')
    run_test("Test Case 5: get_initials(';  ;')", get_initials(';  ;'), '')
