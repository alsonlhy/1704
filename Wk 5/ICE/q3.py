# Name:
# Email ID:

def is_valid_username(username):

    if username == "":
        return False

    if " " in username:
        return False

    if len(username) > 8:
        return False

    special_symbols = "_.!#$%?"
    for ch in username:
        is_valid = (ch in special_symbols) or ch.islower() or ch.isdigit()
        if not is_valid:
            return False


        
