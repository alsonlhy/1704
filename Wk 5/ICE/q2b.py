# Name:
# Email ID:

import q2a

def extract_multiple_email_ids(email_addesses):

    email_split = email_addesses.split(';')


    for email in email_split:

        email_id = q2a.email_id_2(email)

    return email_id


extract_multiple_email_ids("jerry.lee@scis.smu.edu.sg;alan_wong@gmail.com;george_tan@yahoo.com")
