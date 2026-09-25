from q2a import calculate_bmr

tc_num = 1

# Test Case 1
print(f"Test Case {tc_num}")
tc_num += 1
result = calculate_bmr(90.5, 185.0, 55, 'M')
print("Expected:1791 <class 'int'>")
print(f'Actual  :{result} {type(result)}')
print()

# Test Case 2
print(f"Test Case {tc_num}")
tc_num += 1
result = calculate_bmr(65.0, 170.0, 40, 'F')
print("Expected:1351 <class 'int'>")
print(f'Actual  :{result} {type(result)}')
print()

# Test Case 3
print(f"Test Case {tc_num}")
tc_num += 1
result = calculate_bmr(70.0, 180.0, 20, 'M')
print("Expected:1730 <class 'int'>")
print(f'Actual  :{result} {type(result)}')
print()

# Test Case 4
print(f"Test Case {tc_num}")
tc_num += 1
result = calculate_bmr(60.0, 165.0, 35, 'F')
print("Expected:1295 <class 'int'>")
print(f'Actual  :{result} {type(result)}')
print()


