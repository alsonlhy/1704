
# #### b)

def create_email_dict(str_list):

    email_dict = {}

    for i in range(len(str_list)):

        if i % 2 == 0:
            name = str_list[i]
            email = str_list[i+1]
            email_dict[name] = email

    
    return email_dict