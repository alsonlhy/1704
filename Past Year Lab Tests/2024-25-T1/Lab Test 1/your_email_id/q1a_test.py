from q1a import get_hemisphere_volume

print()
print('-' * 20)
print()

print('Test Case 1: get_hemisphere_volume (10.5)')

print()

result = get_hemisphere_volume (10.5) 
print('Expected: 2423.3')
print('Actual:   ' + str(result))

print("\nExpected type of returned value: <class 'float'>")
print('Actual type of returned value:   ' + str(type(result)))

print()
print('-' * 20)
print()

print('Test Case 2: get_hemisphere_volume(5.7)')

print()

result = get_hemisphere_volume(5.7)
print('Expected: 387.67')
print('Actual:   ' + str(result))

print()
print('-' * 20)
print()

