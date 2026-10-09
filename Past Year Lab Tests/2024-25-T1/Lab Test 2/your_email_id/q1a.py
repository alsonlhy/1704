# Name:
# Email ID:

def sum_values_by_weights(lst_tups):

    if lst_tups == []:

        return None

    cost = 0

    for tup in lst_tups:

        if tup[0] <= 10:
            cost += tup[1]

        

    return cost


