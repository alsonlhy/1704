### Q6 More on Lists
## a)
# Write your code below:
##############################################################

def get_all_combinations(str_list, num_list):

    combination = []

    for ch in str_list:
        for i in range(len(num_list)):
            tup = (ch, num_list[i])
            combination.append(tup)


    return combination





##############################################################
# Test Cases to test your code
# DO NOT MODIFY THE TEST CODES

r_list = get_all_combinations(["a", "b"], [1, 2, 3])
print("Expected: [('a', 1), ('a', 2), ('a', 3), ('b', 1), ('b', 2), ('b', 3)]")
print("Actual  : " + str(r_list))
print()
