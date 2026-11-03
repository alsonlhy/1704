def get_reversed_list(num_list):
    new_list = []

    if num_list == []:

        return []

    for num in num_list:

        if num == 0.0:
            new_num = num
        elif num < 0.0:
            new_num = abs(num)
        else:
            new_num = -num

        new_list.append(new_num)
        reversed_list = new_list[::-1]

    return reversed_list

    