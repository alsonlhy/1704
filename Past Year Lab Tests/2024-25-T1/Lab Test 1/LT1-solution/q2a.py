# Name:
# Email ID:

def count_short_strings(str_list, n):
    # Modify the code below.
    count = 0
    for a_str in str_list:
        if len(a_str) < n:
            count += 1
    
    return count