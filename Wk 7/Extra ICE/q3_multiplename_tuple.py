def find_students(namelist):

    newlist = []
    existing_lastname = []

    for tup in namelist:

        lastname = tup[1]

        if lastname not in existing_lastname:
            existing_lastname.append(lastname)
            newlist.append(tup)

    return newlist


print(find_students([("James", "Wong"), ("Lily", "Khoo"), ("Peter", "Wong"), ("George", "Lim")]))

# Worst case: O(n^2); n*(n-1)/2