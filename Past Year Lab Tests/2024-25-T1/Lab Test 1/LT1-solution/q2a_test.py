from q2a import count_short_strings

print()
print('-' * 20)
print()

print("Test Case 1: count_short_strings(['abcd', '123', '**', '!@#$%^'], 4)")

print()

result = count_short_strings(['abcd', '123', '**', '!@#$%^'], 4)
print('Expected: 2')
print('Actual:   ' + str(result))

print("Expected type of returned value: <class 'int'>")
print('Actual type of returned value:   ' + str(type(result)))

print()
print('-' * 20)
print()

print("Test Case 2: count_short_strings(['+++++', 'purple', 'pear', 'tiger'], 5)")

print()

result = count_short_strings(['+++++', 'purple', 'pear', 'tiger'], 5)
print('Expected: 1')
print('Actual:   ' + str(result))


print()
print('-' * 20)
print()

print("Test Case 3: count_short_strings(['1234567890', 'abcdefg'], 1)")

print()

result = count_short_strings(['1234567890', 'abcdefg'], 1)
print('Expected: 0')
print('Actual:   ' + str(result))

print()
print('-' * 20)
print()

print("Test Case 4: count_short_strings([''], 1)")

print()

result = count_short_strings([''], 1)
print('Expected: 1')
print('Actual:   ' + str(result))

print()
print('-' * 20)
print()

print("Test Case 5: count_short_strings([], 1)")

print()

result = count_short_strings([], 1)
print('Expected: 0')
print('Actual:   ' + str(result))

print()
print('-' * 20)
print()