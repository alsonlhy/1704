from q3b import read_into_dict

# Test cases used to test your function

print('\nTestcase 1')
print('-' * 10)
print("Expected: {'SMU': 'Singapore Management University', 'NUS': 'National University of Singapore', 'NTU': 'National University of Technology', 'SUTD': 'Singapore University of Technology and Design', 'SIM': 'Singapore Intitute of Management'}")
filename = 'acronyms.txt'
result_dict = read_into_dict(filename)
print('Actual:   ' + str(result_dict))
