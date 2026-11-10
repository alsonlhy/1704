from q4 import get_document_pair



if __name__ == '__main__':
    print("Test Case for Q3")
    print('-' * 10)
    print('Test case 1')
    print('Expected:', ('D2', 'D4', 3), 'or', ('D4', 'D2', 3))
    result = get_document_pair('documents.txt')
    print('Actual:  ', result)
    print()

    