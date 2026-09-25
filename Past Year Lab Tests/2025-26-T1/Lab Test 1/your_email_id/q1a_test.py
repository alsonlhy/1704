from q1a import is_food_safe

print()
print('-' * 20)
print()

# Safe because temperature is within 75–100°C
print("Test Case 1: is_food_safe(80.0, 1)")

print()

result = is_food_safe(80.0, 1)
print('Expected: True')
print('Actual:   ' + str(result))

print("Expected type of returned value: <class 'bool'>")
print('Actual type of returned value:   ' + str(type(result)))

print()
print('-' * 20)
print()

# Safe because held at 60–74.9°C for at least 2 minutes
print("Test Case 2: is_food_safe(74.5, 2)")

print()

result = is_food_safe(74.5, 2)
print('Expected: True')
print('Actual:   ' + str(result))
print("Expected type of returned value: <class 'bool'>")
print('Actual type of returned value:   ' + str(type(result)))

print()
print('-' * 20)
print()

# Not held long enough
print("Test Case 3: is_food_safe(74.5, 1)")

print()

result = is_food_safe(74.5, 1)
print('Expected: False')
print('Actual:   ' + str(result))
print("Expected type of returned value: <class 'bool'>")
print('Actual type of returned value:   ' + str(type(result)))

print()
print('-' * 20)
print()

# Temperature too low
print("Test Case 4: is_food_safe(58.0, 10)")

print()

result = is_food_safe(58.0, 10)
print('Expected: False')
print('Actual:   ' + str(result))
print("Expected type of returned value: <class 'bool'>")
print('Actual type of returned value:   ' + str(type(result)))

print()
print('-' * 20)
print()

# Safe due to high temperature
print("Test Case 5: is_food_safe(100.0, 0)")

print()

result = is_food_safe(100.0, 0)
print('Expected: True')
print('Actual:   ' + str(result))
print("Expected type of returned value: <class 'bool'>")
print('Actual type of returned value:   ' + str(type(result)))

print()
print('-' * 20)
print()

# Too hot – unsafe
print("Test Case 6: is_food_safe(101.0, 2)")

print()

result = is_food_safe(101.0, 2)
print('Expected: False')
print('Actual:   ' + str(result))
print("Expected type of returned value: <class 'bool'>")
print('Actual type of returned value:   ' + str(type(result)))

print()
print('-' * 20)
print()