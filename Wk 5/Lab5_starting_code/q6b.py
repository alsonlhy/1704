### Q6 More on Lists
## b)
# Write your code below:
##############################################################

def get_larger_numbers(num_list1, num_list2):

    larger = []
    check_num = False

    for num1 in num_list1:

        for num2 in num_list2:
            if num1 > num2:
                check_num = True
            else:
                check_num = False

        if check_num == True:
            larger.append(num1)

    return larger






##############################################################
# Test Cases to test your code
# DO NOT MODIFY THE TEST CODES

r_list = get_larger_numbers([4, 6, 10], [1, 3, 5])
print("Expected: [6, 10]")
print("Actual  : " + str(r_list))
print()
