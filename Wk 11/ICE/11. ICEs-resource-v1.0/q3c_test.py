from q3c import reverse_dict

# Test cases used to test your function

print('\nTestcase 1')
print('-' * 10)
print("Expected: {'swimming': 'Monday', 'basketball': 'Tuesday', 'tennis': 'Wednesday', 'yoga': 'Thursday', 'gymnastics': 'Friday'}")
my_dict = {'Monday': 'swimming', 'Tuesday': 'basketball', 'Wednesday': 'tennis', 'Thursday': 'yoga', 'Friday': 'gymnastics'}
result_dict = reverse_dict(my_dict)
print('Actual:   ' + str(result_dict))
