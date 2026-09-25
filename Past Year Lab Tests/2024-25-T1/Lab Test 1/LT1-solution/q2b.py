# Name:
# Email ID:

def get_longest_string(str_list):
    # Modify the code below.
    if str_list == []:
        return None
    
    longest_str = ''
    for a_str in str_list:
        if len(a_str) >= len(longest_str):
            longest_str = a_str
            
    return (longest_str, len(longest_str))
