from q1c import check_numbers

print('Testcase 1 - True')
print('-' * 10)
print('Expected: True')
list1 = [3, 8, 10, 15, 16]
list2 = [9, 3, 2, 5]
result = check_numbers(list1,list2)
print('Actual:   ' + str(result))

print('\nTestcase 2 - False')
print('-' * 10)
print('Expected: False')
list1 = [3, 8, 10, 6, 2, 5]
list2 = [9, 3, 7]
result = check_numbers(list1,list2)
print('Actual:   ' + str(result))
