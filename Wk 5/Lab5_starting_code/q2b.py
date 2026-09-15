### Q2 List of Numbers
## b)
# Write your code below:
##############################################################

def all_older_than(age_list, n):


    for num in age_list:
        if num > n:
            age = True

        else:
            age = False

    return age






##############################################################
# Test Cases to test your code
# DO NOT MODIFY THE TEST CODES

print('Test Case 1')
print('-' * 11)
print('Expected: True')
print('Actual:   ' + str(all_older_than([24, 36, 45, 21], 20)))

print('\nTest Case 2')
print('-' * 11)
print('Expected: False')
print('Actual:   ' + str(all_older_than([24, 36, 45, 21], 23)))