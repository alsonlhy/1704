### Q2 List of Numbers
## d)
# Write your code below:
##############################################################
import math


def check_prime(n):

    if n <= 1:
        return False

    if n in (2,3):
        return True

    if n % 2 == 0:
        return False

    for i in range(3, math.isqrt(n)+ 1, 2):
        if n % i == 0:
            return False

    return True

def get_prime_numbers(num_list, sep):

    string = ""
    check = False


    for num in num_list[:len(num_list)-1]:
        if check == False and check_prime(num) == True:
            string += str(num)
            check = True

        elif check == True and check_prime(num) == True:
            string += sep + str(num)


    return string





##############################################################
# Test Cases to test your code
# DO NOT MODIFY THE TEST CODES

print('Test Case 1')
print('-' * 11)
print('Expected: 2-7-11-19')
print('Actual:   ' + str(get_prime_numbers([2, 4, 7, 9, 11, 16, 19, 21], '-')))

print('\nTest Case 2')
print('-' * 11)
print('Expected: 3')
print('Actual:   ' + str(get_prime_numbers([3, 4, 8, 9, 12, 16], '*')))
