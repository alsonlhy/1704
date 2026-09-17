### Q6 More on Lists
## c)
# Write your code below:
##############################################################

def get_non_common_strings(str_list1, str_list2):

    uncommon = []

    for ch1 in str_list1:

        if ch1 not in str_list2:
            uncommon.append(ch1)

    # for ch2 in str_list2:
    #     if ch2 not in str_list1:
    #         uncommon.append(ch2)

    return uncommon

                

            







##############################################################
# Test Cases to test your code
# DO NOT MODIFY THE TEST CODES

r_list = get_non_common_strings(["a", "b", "c", "d"], ["b", "d", "e", "f"])
print("Expected: ['a', 'c', 'e', 'f']")
print("Actual  : " + str(r_list))
print()