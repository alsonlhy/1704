### Q2 List of Numbers
## e)
# Write your code below:
##############################################################

def calculate_sums(num_list):

    list_add = ""
    num = []

    for i in range(len(num_list)):

        numeral = num_list[i]

        if numeral == num_list[0]:
            num.append(numeral)

        else:
            for i in range(1, len(num_list)):
                total = num_list[i] + num_list[i-1]
                num.append(total)

    return num
            






##############################################################
# Test Cases to test your code
# DO NOT MODIFY THE TEST CODES

print('Test Case 1')
print('-' * 11)
print('Expected: [2, 5, 11, 12, 17]')
print('Actual:   ' + str(calculate_sums([2, 3, 6, 1, 5])))

print('\nTest Case 2')
print('-' * 11)
print('Expected: []')
print('Actual:   ' + str(calculate_sums([])))