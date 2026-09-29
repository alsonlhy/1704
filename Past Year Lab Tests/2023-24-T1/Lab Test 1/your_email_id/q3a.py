# Name:
# Email ID:

def is_partially_compliant(table):

    unique_year = []

    for tup in table:

        if tup[1] not in unique_year:

            unique_year.append(tup[1])

    if len(unique_year) != 1 and len(unique_year) != 2:

        return False

    if len(unique_year) == 2:
        if not(unique_year[0] == unique_year[1]+1 or unique_year[0] == unique_year[1]-1):

            return False


    schools = ['scis', 'bus', 'acc', 'sosc', 'law', 'eco']
    schools_cnt = [0, 0, 0, 0, 0, 0]
    for tup in table:
        for i in range(len(schools)):
            if tup[2] == schools[i]:
                schools_cnt[i] += 1


    for i in range(len(schools_cnt)):
        if schools_cnt[i] > 2:
            return False

    return True