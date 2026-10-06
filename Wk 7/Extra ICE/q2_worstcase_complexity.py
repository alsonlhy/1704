# Q2: Smallest Difference [ *** ]
# Implement and analyze the worst-case complexity of a function called find_smallest_diff that takes in a list my_list of n integers. The function returns the smallest difference (>=0) between any two integers in my_list. For example:
# find_smallest_diff([1, 2, 3, 4]) returns 1.
# find_smallest_diff([1, 3, 1, 4]) returns 0.
# find_smallest_diff([4,7,1,9,33,77,55,44,22,49,88]) returns 2.


def find_smallest_diff_slow(my_list):
    smallest = abs(my_list[0] - my_list[1])
    for i in range(len(my_list)):
        for j in range(i + 1, len(my_list)):
            smallest = min(smallest, abs(my_list[i] - my_list[j]))
    return smallest

# Worst case: O(n^2)