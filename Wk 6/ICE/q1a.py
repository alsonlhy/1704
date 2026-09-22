# Name:
# Email ID:

def get_larger_values(num_list):

    new_list = []

    average = sum(num_list) / len(num_list)

    for num in num_list:

        if num > average:
            new_list.append(num)

    
    return new_list

