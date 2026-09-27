# Name:
# Email ID:

def count_non_digits(str_list):

    if str_list == []:

        return []

    new_list = []

    for string in str_list:

        count = 0

        for ch in string:

            if ch.isdigit() == False:
                count += 1

        new_list.append(count) 

    
    return new_list