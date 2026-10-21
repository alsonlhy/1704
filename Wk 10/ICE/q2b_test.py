from q2b import check_same_author

# Test cases used to test your function
print('\nTest case 1:')
print('------------')
print("Expected: False")
filename = 'books-1.txt'
result = check_same_author(filename)
print('Actual:   ' + str(result))

print('\nTest case 2:')
print('------------')
print("Expected: True")
filename = 'books-2.txt'
result = check_same_author(filename)
print('Actual:   ' + str(result))

print('\nTest case 3:')
print('------------')
print("Expected: False")
filename = 'books-3.txt'
result = check_same_author(filename)
print('Actual:   ' + str(result))
print()
