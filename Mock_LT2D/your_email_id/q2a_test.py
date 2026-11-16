from q2a import get_unreturned

if __name__ == '__main__':
    print('Test cases for Q2A')
    print('-' * 20)
    print('Test case 1: get_unreturned("loans-1.txt")')
    print('Expected:', [('M02', 'Dune'), ('M01', 'Emma'), ('M01', 'Dracula')])
    print('Actual:  ', get_unreturned('loans-1.txt'))
    print()
    print('Test case 2: get_unreturned("loans-2.txt")')
    print('Expected:', [])
    print('Actual:  ', get_unreturned('loans-2.txt'))
    print()
