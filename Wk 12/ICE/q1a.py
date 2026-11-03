# ### Q1: Emails
# #### a)

def retrieve_email(email_dict, name):
    
    if name in email_dict:
        return email_dict[name]

    else:
        return None