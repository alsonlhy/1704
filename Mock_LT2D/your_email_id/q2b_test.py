from q2b import get_member_summary

if __name__ == '__main__':
    print('Test cases for Q2B')
    print('-' * 20)
    print('Test case 1: get_member_summary("loans-1.txt")')
    print('Expected:', {'M01': (3, 2), 'M02': (2, 1), 'M03': (1, 0)})
    print('Actual:  ', get_member_summary('loans-1.txt'))
    print()
    print('Test case 2: get_member_summary("loans-2.txt")')
    print('Expected:', {})
    print('Actual:  ', get_member_summary('loans-2.txt'))
    print()
