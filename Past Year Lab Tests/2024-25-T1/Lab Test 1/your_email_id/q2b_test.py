from q2b import get_longest_string

print()
print('-' * 20)
print()

print("Test Case 1: get_longest_string(['grape', 'lime', 'pear'])")

print()

result = get_longest_string(['grape', 'lime', 'pear'])
print("Expected: ('grape', 5)")
print('Actual:   ' + str(result))

print("Expected type of returned value: <class 'tuple'>")
print('Actual type of returned value:   ' + str(type(result)))

print()
print('-' * 20)
print()

print("Test Case 2: get_longest_string(['grape', 'apple', 'pear'])")

print()

result = get_longest_string(['grape', 'apple', 'pear'])
print("Expected: ('apple', 5)")
print('Actual:   ' + str(result))


print()
print('-' * 20)
print()

print("Test Case 3: get_longest_string(['', 'orange', 'durian'])")

print()

result = get_longest_string(['', 'orange', 'durian'])
print("Expected: ('durian', 6)")
print('Actual:   ' + str(result))

print()
print('-' * 20)
print()

print("Test Case 4: get_longest_string([''])")

print()

result = get_longest_string([''])
print("Expected: ('', 0)")
print('Actual:   ' + str(result))

print()
print('-' * 20)
print()

print("Test Case 5: get_longest_string([])")

print()

result = get_longest_string([])
print('Expected: None')
print('Actual:   ' + str(result))

print("Expected type of returned value: <class 'NoneType'>")
print('Actual type of returned value:   ' + str(type(result)))

print()
print('-' * 20)
print()