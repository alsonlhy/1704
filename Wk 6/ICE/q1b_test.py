from q1b import merge_list

print('Testcase 1 - list1 and list2 have the same length')
print('-' * 10)
print('Expected: [1, 9, 3, 5, 10, 2]')
list1 = [1, 3, 10]
list2 = [9, 5, 2]
result = merge_list(list1,list2)
print('Actual:   ' + str(result))

print('\nTestcase 2 - list1 is longer than list2')
print('-' * 10)
print('Expected: [1, 9, 3, 5, 10, 2, 15, 4, 7, 12]')
list1 = [1, 3, 10, 15, 4, 7, 12]
list2 = [9, 5, 2]
result = merge_list(list1,list2)
print('Actual:   ' + str(result))

print('\nTestcase 3 - list2 is longer than list1')
print('-' * 10)
print('Expected: [4, 8, 2, 1, 6, 3, 9, 5, 88]')
list1 = [4, 2, 6]
list2 = [8, 1, 3, 9, 5, 88]
result = merge_list(list1,list2)
print('Actual:   ' + str(result))