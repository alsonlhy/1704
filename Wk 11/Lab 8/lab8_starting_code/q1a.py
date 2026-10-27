## Q1a Substitution Cipher
# write your code below

def encrypt(my_dict, msg):

    new_msg = ""

    for letter in msg:

        if letter == ' ':
            new_msg += ' '

        else: 
            new_msg += my_dict[letter]

    return new_msg