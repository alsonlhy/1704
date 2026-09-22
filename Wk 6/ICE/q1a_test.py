from q1a import get_larger_values

print('Testcase 1')
print('-' * 10)
print('Expected: [3.5, 5.5]')
num_list = [2.5,3.5,5.5,1.0]
result = get_larger_values(num_list)
print('Actual:   ' + str(result))

print('\nTestcase 2')
print('-' * 10)
print('Expected: [3.5]')
num_list = [2.5,3.5,3]
result = get_larger_values(num_list)
print('Actual:   ' + str(result))

print('\nTestcase 3')
print('-' * 10)
print('Expected: []')
num_list = [4.1]
result = get_larger_values(num_list)
print('Actual:   ' + str(result))