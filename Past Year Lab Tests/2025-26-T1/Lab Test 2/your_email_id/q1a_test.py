from q1a import get_specific_tuples

# Tuples of same length
print()
a_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
print('a_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]')
print()

print("\nTest Case 1: get_specific_tuples(a_list, 5)")
print("-------------------------------------------")
result = get_specific_tuples(a_list, 5)
print('Expected: [(4, 5, 6), (7, 8, 9)]')
print('Actual:   ' + str(result))

print("\nExpected type of returned value: <class 'list'>")
print('Actual type of returned value:   ' + str(type(result)))
print()


print("\nTest Case 2: get_specific_tuples(a_list, 15)")
print("-------------------------------------------")
result = get_specific_tuples(a_list, 15)
print('Expected: [(7, 8, 9)]')
print('Actual:   ' + str(result))
print()


print("\nTest Case 3: get_specific_tuples(a_list, 20)")
print("-------------------------------------------")
result = get_specific_tuples(a_list, 20)
print('Expected: []')
print('Actual:   ' + str(result))


print()
print("\nTest Case 4: get_specific_tuples([], 10)")
print("-------------------------------------------")
result = get_specific_tuples([], 10)
print('Expected: []')
print('Actual:   ' + str(result))
print()

# Tuples of different length
print()
b_list = [(1, 2, 3), (4, 5, 6, 0), (7, 8, 9, 10, 11, 12), (10, 4)]
print('b_list = [(1, 2, 3), (4, 5, 6, 0), (7, 8, 9, 10, 11, 12), (10, 4)]')
print()

print("\nTest Case 5: get_specific_tuples(b_list, 14)")
print("-------------------------------------------")
result = get_specific_tuples(b_list, 14)
print('Expected: [(7, 8, 9, 10, 11, 12), (10, 4)]')
print('Actual:   ' + str(result))
print()


print("\nTest Case 6: get_specific_tuples(b_list, 15)")
print("-------------------------------------------")
result = get_specific_tuples(b_list, 15)
print('Expected: [(7, 8, 9, 10, 11, 12)]')
print('Actual:   ' + str(result))
print()

print("\nTest Case 7: get_specific_tuples(b_list, 20)")
print("-------------------------------------------")
result = get_specific_tuples(b_list, 20)
print('Expected: []')
print('Actual:   ' + str(result))
print()