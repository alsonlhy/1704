from q3 import count_emails

if __name__ == '__main__':
    # #####################################
    # Test Cases of Q3
    print('\nTestcase 1')
    print('-' * 10)
    count = count_emails('emails-1.txt', (12, 30), (14, 0), 'joe@abc.com')
    print("Expected: 3")
    print('Actual:   ' + str(count))

    print('\nTestcase 2')
    print('-' * 10)
    count = count_emails('emails-2.txt', (11, 0), (14, 0), 'joe@abc.com')
    print("Expected: 2")
    print('Actual:   ' + str(count))