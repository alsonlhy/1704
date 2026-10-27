## Q1b Substitution Cipher
# write your code below

def decrypt(my_dict, encrypted_msg):

    ori_msg = ""

    for letter in encrypted_msg:

        if letter == " ":
            ori_msg += " "

        else:
            ori_msg += my_dict[letter]

    return ori_msg
