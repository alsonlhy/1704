from q1b import compute_plan_cost

print()
print('-' * 20)
print()

# Valid plan: within quota (no extra charges)
print("Test Case 1: compute_plan_cost('Lite', 50.5)")

print()

result = compute_plan_cost('Lite', 50.5)
print('Expected: 10')
print('Actual:   ' + str(result))

print("Expected type of returned value: <class 'int'>")
print('Actual type of returned value:   ' + str(type(result)))

print()
print('-' * 20)
print()

# Valid plan: over quota (extra charges apply)
print("Test Case 2: compute_plan_cost('Standard', 232.1)")

print()

result = compute_plan_cost('Standard', 232.1)
print('Expected: 20')
print('Actual:   ' + str(result))

print("Expected type of returned value: <class 'int'>")
print('Actual type of returned value:   ' + str(type(result)))

print()
print('-' * 20)
print()

# Valid plan: edge case at exact quota
print("Test Case 3: compute_plan_cost('Pro', 900.0)")

print()

result = compute_plan_cost('Pro', 900.0)
print('Expected: 50')
print('Actual:   ' + str(result))

print("Expected type of returned value: <class 'int'>")
print('Actual type of returned value:   ' + str(type(result)))

print()
print('-' * 20)
print()

# Invalid plan: return message
print("Test Case 4: compute_plan_cost('Basic', 205.6)")

print()

result = compute_plan_cost('Basic', 205.6)
print('Expected: Invalid plan selected')
print('Actual:   ' + str(result))

print("Expected type of returned value: <class 'str'>")
print('Actual type of returned value:   ' + str(type(result)))

print()
print('-' * 20)
print()

# Zero data usage
print("Test Case 5: compute_plan_cost('Standard', 0.0)")

print()

result = compute_plan_cost('Standard', 0.0)
print('Expected: 20')
print('Actual:   ' + str(result))

print("Expected type of returned value: <class 'int'>")
print('Actual type of returned value:   ' + str(type(result)))

print()
print('-' * 20)
print()

# Valid plans: edge case slightly over quota (pro-rated charges)
print("Test Case 6: compute_plan_cost('Lite', 100.1)")

print()

result = compute_plan_cost('Lite', 100.1)
print('Expected: 10.5')
print('Actual:   ' + str(result))

print("Expected type of returned value: <class 'float'>")
print('Actual type of returned value:   ' + str(type(result)))

print()
print('-' * 20)
print()

print("Test Case 7: compute_plan_cost('Standard', 333.33)")

print()

result = compute_plan_cost('Standard', 333.33)
print('Expected: 119.99')
print('Actual:   ' + str(result))

print("Expected type of returned value: <class 'float'>")
print('Actual type of returned value:   ' + str(type(result)))

print()
print('-' * 20)
print()

print("Test Case 8: compute_plan_cost('Pro', 999.991)")

print()

result = compute_plan_cost('Pro', 999.991)
print('Expected: 149.99')
print('Actual:   ' + str(result))

print("Expected type of returned value: <class 'float'>")
print('Actual type of returned value:   ' + str(type(result)))

print()
print('-' * 20)
print()


