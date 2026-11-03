# ### Q1: Emails
# #### a)

from q1a import retrieve_email
    
# Test cases used to test your function

print('\nTestcase 1')
print('-' * 10)
my_dict = {'Jack':'jack@gmail.com', 'Peter':'peter@smu.edu.sg'}
name = 'Jack'
print("Expected: jack@gmail.com")
print('Actual:   ' + str(retrieve_email(my_dict, name)))

print('\nTestcase 2')
print('-' * 10)
my_dict = {'Jack':'jack@gmail.com', 'Peter':'peter@smu.edu.sg'}
a_name = 'John'
print("Expected: None")
print('Actual:   ' + str(retrieve_email(my_dict, a_name)))
