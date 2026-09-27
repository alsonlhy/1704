# Name:
# Email ID:

def get_digits_of_even_index(my_str):

    if my_str == []:
        return []

    new_str = ""

    for i in range(len(my_str)):

        if i % 2 == 0 and my_str[i].isdigit():
            new_str = new_str + my_str[i]

    
    return new_str