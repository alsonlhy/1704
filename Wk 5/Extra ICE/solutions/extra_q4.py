# Name:
# Email ID:

# Solution 1: index-based, checking whether each neighbour exists

def sum_of_neighbors(input_list):
    list_to_return = []

    for i in range(len(input_list)):
        # start with the element itself
        total = input_list[i]

        # add the left neighbour, if there is one
        if i > 0:
            total = total + input_list[i - 1]

        # add the right neighbour, if there is one
        if i < len(input_list) - 1:
            total = total + input_list[i + 1]

        list_to_return.append(total)

    return list_to_return

# Solution 2: let the slice operator handle the boundaries for us
def sum_of_neighbors(input_list):
    list_to_return = []

    for i in range(len(input_list)):
        # a slice never raises IndexError: it just returns fewer elements
        # near the two ends of the list
        if i == 0:
            neighbourhood = input_list[0:2]
        else:
            neighbourhood = input_list[i - 1:i + 2]

        total = 0
        for number in neighbourhood:
            total = total + number

        list_to_return.append(total)

    return list_to_return
