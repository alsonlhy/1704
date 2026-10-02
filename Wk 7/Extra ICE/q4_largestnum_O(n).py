def largest_num(numlist):

    sorted_numlist = sorted(numlist)

    largest_10 = sorted_numlist[-1:-11:-1]

    return largest_10[::-1]


print(largest_num([2,4,5,6,7,8,9,10,13,15,17,11,21,25]))