# Name: 
# Email ID: 

def reverse_dict(my_dict):

    new_dict = {}

    for day, activity in my_dict.items():
        new_dict[activity] = day

    return new_dict


