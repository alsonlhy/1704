from q5 import get_strings_with_digits

print('\nTestcase 1')
print('-' * 10)
print("Expected: ['ab12', 'IS111']")
str_list = ['ab12', 'IS111', '9', 'X7Z', 'k', 'lmn']
result = get_strings_with_digits(str_list, 3)
print('Actual:   ' + str(result))

print('\nTestcase 2')
print('-' * 10)
print("Expected: ['ab12', 'IS111', '9']")
str_list = ['ab12', 'IS111', '9', 'X7Z', 'k', 'lmn']
result = get_strings_with_digits(str_list, 5)
print('Actual:   ' + str(result))

print('\nTestcase 3')
print('-' * 10)
print("Expected: ['ab12', 'IS111', '9', 'X7Z', 'k', 'lmn']")
str_list = ['ab12', 'IS111', '9', 'X7Z', 'k', 'lmn']
result = get_strings_with_digits(str_list, 8)
print('Actual:   ' + str(result))

