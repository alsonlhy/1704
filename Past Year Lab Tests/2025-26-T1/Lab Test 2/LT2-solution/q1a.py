# Name:
# Email ID:

def get_specific_tuples(tup_list, num):
    # Modify the code below.
    list_to_return = []
    
    for tup in tup_list:
        if tup[0] + tup[1] >= num:
            list_to_return.append(tup)

    return list_to_return
