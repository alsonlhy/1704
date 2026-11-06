
# #### c)

def add_new_email(email_dict, pair):
    
    old_value = ""

    if pair[0] in email_dict:
        old_value += email_dict[pair[0]]

        email_dict[pair[0]] = pair[1]

    else:
        email_dict[pair[0]] = pair[1]

        return None

    return old_value


