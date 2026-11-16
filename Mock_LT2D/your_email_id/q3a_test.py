from q3a import get_fees

if __name__ == '__main__':
    print('Test cases for Q3A')
    print('-' * 20)
    print('Test case 1: get_fees("carpark-1.txt")')
    print('Expected:', {'SKB88C': 1.8, 'SGA1234A': 3.0})
    print('Actual:  ', get_fees('carpark-1.txt'))
    print()
    print('Test case 2: get_fees("carpark-2.txt")')
    print('Expected:', {})
    print('Actual:  ', get_fees('carpark-2.txt'))
    print()
    print('Test case 3: get_fees("carpark-3.txt")')
    print('Expected:', {'B2': 3.0, 'A1': 3.6})
    print('Actual:  ', get_fees('carpark-3.txt'))
    print()
