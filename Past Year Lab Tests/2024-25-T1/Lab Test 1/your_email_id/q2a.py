# Name:
# Email ID:

def count_short_strings(str_list, n):

    count = 0

    for string in str_list:

        if len(string) < n:
            count += 1
    
    return count