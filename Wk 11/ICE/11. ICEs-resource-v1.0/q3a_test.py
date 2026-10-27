from q3a import convert_to_dict

# Test cases used to test your function

print('\nTestcase 1')
print('-' * 10)
print("Expected: {1: 'apple', 2: 'banana', 4: 'durian', 8: 'orange', 3: 'peach'}")
tup_list = [(1, 'apple'), (2, 'banana'), (4, 'durian'), (8, 'orange'), (3, 'peach')]
result_dict = convert_to_dict(tup_list)
print('Actual:   ' + str(result_dict))
