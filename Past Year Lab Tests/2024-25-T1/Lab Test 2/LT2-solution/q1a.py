# Name:
# Email ID:

def sum_values_by_weights(lst_tups):
    # Replace the code below with your implementation.
    if lst_tups == []:
        return None
    
    dollar_sum = 0
    for tup in lst_tups:
        w = tup[0]
        p = tup[1]
        if w <= 10:
            dollar_sum += p
            
    return dollar_sum


