# Name:
# Email ID:

# def extract_email_id(email_address):

#     for i in range(len(email_address)):

#         ch = email_address[i]
#         if ch == "@":

#             return email_address[0:i]

#     return ''





def email_id_2(email_address):

    parts = email_address.split('@')

    if len(parts) == 2:
        return parts[0]

    else:
        return ""
