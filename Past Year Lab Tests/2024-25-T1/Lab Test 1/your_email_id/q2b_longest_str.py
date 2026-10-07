# Name:
# Email ID:

def get_longest_string(str_list):

    if str_list == []:

        return None


    tup = (str_list[0], len(str_list[0]))

    for string in str_list:

        if len(string) >= tup[1]:

            tup = (string, len(string))
    
    return tup
