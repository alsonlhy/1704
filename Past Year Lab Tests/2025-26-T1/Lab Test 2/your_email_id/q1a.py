# Name:
# Email ID:

def get_specific_tuples(tup_list, num):

    new_list = []

    for tup in tup_list:
        if tup[0] + tup[-1] >= num:
            new_list.append((tup))

    
    return new_list
