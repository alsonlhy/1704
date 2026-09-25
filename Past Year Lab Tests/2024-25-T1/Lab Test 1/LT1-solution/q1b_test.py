from q1b import is_allowed_in_carryon

print()
print('-' * 20)
print()

print('Test Case 1: is_allowed_in_carryon("Electronics", 3)')

print()

result = is_allowed_in_carryon("Electronics", 3)
print('Expected: True')
print('Actual:   ' + str(result))

print("\nExpected type of returned value: <class 'bool'>")
print('Actual type of returned value:   ' + str(type(result)))

print()
print('-' * 20)
print()

print('Test Case 2: is_allowed_in_carryon("Weapons", 1)')

print()

result = is_allowed_in_carryon("Weapons", 1)
print('Expected: False')
print('Actual:   ' + str(result))

print("\nExpected type of returned value: <class 'bool'>")
print('Actual type of returned value:   ' + str(type(result)))

print()
print('-' * 20)
print()

print('Test Case 3: is_allowed_in_carryon("Liquids", 75)')

print()

result = is_allowed_in_carryon("Liquids", 75)
print('Expected: True')
print('Actual:   ' + str(result))

print("\nExpected type of returned value: <class 'bool'>")
print('Actual type of returned value:   ' + str(type(result)))

print()
print('-' * 20)
print()

print('Test Case 4: is_allowed_in_carryon("Liquids", 120)')

print()

result = is_allowed_in_carryon("Liquids", 120)
print('Expected: False')
print('Actual:   ' + str(result))

print("\nExpected type of returned value: <class 'bool'>")
print('Actual type of returned value:   ' + str(type(result)))

print()
print('-' * 20)
print()

print('Test Case 5: is_allowed_in_carryon("Food", 2)')

print()

result = is_allowed_in_carryon("Food", 2)
print('Expected: True')
print('Actual:   ' + str(result))

print("\nExpected type of returned value: <class 'bool'>")
print('Actual type of returned value:   ' + str(type(result)))

print()
print('-' * 20)
print()

print('Test Case 6: is_allowed_in_carryon("Tools", 1)')

print()

result = is_allowed_in_carryon("Tools", 1)
print('Expected: Contact Staff')
print('Actual:   ' + str(result))

print("\nExpected type of returned value: <class 'str'>")
print('Actual type of returned value:   ' + str(type(result)))

print()
print('-' * 20)
print()

print('Test Case 7: is_allowed_in_carryon("Aerosols", 1)')

print()

result = is_allowed_in_carryon("Aerosols", 1)
print('Expected: Contact Staff')
print('Actual:   ' + str(result))

print("\nExpected type of returned value: <class 'str'>")
print('Actual type of returned value:   ' + str(type(result)))

print()
print('-' * 20)
print()



