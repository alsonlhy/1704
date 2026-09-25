from q2b import find_people_in_range

idx = 1
# Test Case 1: No one in range
print(f"Test Case {idx}")
idx += 1
people_1 = [
    ("Bob", 55.0, 160.0, 25, 'F'),   # BMR: 1264
    ("Jane", 60.0, 165.0, 30, 'F')   # BMR: 1320
]
result = find_people_in_range(people_1, (1400, 2000))
print(f"Expected:|| <class 'str'>")
print(f'Actual  :|{result}| {type(result)}')
print()

# Test Case 2: One person in range
print(f"Test Case {idx}")
idx += 1
people_2 = [
    ("Apple", 45.0, 160.0, 25, 'F'),   # BMR: 1164
    ("Orange", 75.5, 178.5, 35, 'F')   # BMR: 1534
]
result = find_people_in_range(people_2, (1000, 1500))
print(f"Expected:|1-Apple(1164)| <class 'str'>")
print(f'Actual  :|{result}| {type(result)}')
print()

# Test Case 3: Multiple people in range, checking order
print(f"Test Case {idx}")
idx += 1
people_3 = [
    ("Apple", 85.0, 190.0, 22, 'M'),    # BMR: 1932
    ("Orange", 55.0, 160.0, 25, 'F'),   # BMR: 1264
    ("Pear", 60.0, 165.0, 30, 'F') ,    # BMR: 1320
    ("Durian", 90.0, 165.0, 45, 'M')    # BMR: 1711

]
result = find_people_in_range(people_3, (1300, 1800))
print(f"Expected:|1-Pear(1320)-2-Durian(1711)| <class 'str'>")
print(f'Actual  :|{result}| {type(result)}')
print()

# Test Case 4: exclude the max
print(f"Test Case {idx}")
idx += 1
people_4 = [
    ("Apple", 85.0, 190.0, 22, 'M'),    # BMR: 1932
    ("Orange", 55.0, 160.0, 25, 'F'),   # BMR: 1264
    ("Pear", 60.0, 165.0, 30, 'F') ,    # BMR: 1320
    ("Durian", 90.0, 165.0, 45, 'M'),   # BMR: 1711
    ("Grape", 65.0, 190.0, 45, 'M'),    # BMR: 1617
]
result = find_people_in_range(people_4, (1264, 1932))
print(f"Expected:|1-Orange(1264)-2-Pear(1320)-3-Durian(1711)-4-Grape(1617)| <class 'str'>")
print(f'Actual  :|{result}| {type(result)}')
print()