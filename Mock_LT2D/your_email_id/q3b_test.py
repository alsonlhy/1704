from q3b import get_longest_stay

if __name__ == '__main__':
    print('Test cases for Q3B')
    print('-' * 20)
    print('Test case 1: get_longest_stay("carpark-1.txt")')
    print('Expected:', ('SGA1234A', 91))
    print('Actual:  ', get_longest_stay('carpark-1.txt'))
    print()
    print('Test case 2: get_longest_stay("carpark-2.txt")')
    print('Expected:', None)
    print('Actual:  ', get_longest_stay('carpark-2.txt'))
    print()
    print('Test case 3: get_longest_stay("carpark-3.txt")')
    print('Expected:', ('A1', 80))
    print('Actual:  ', get_longest_stay('carpark-3.txt'))
    print()
