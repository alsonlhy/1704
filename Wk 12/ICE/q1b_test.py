
# #### b)
# SOLUTION 1

from q1b import create_email_dict
    

# Test cases used to test your function

print('\nTestcase')
print('-' * 10)
my_list = ["Jack", "jack@gmail.com", "Mary", "mary.loh@smu.edu.sg", "John", "john.smith@microsoft.com"]
result_dict = {'Jack': 'jack@gmail.com', 'Mary': 'mary.loh@smu.edu.sg', 'John': 'john.smith@microsoft.com'}
print("Expected: " + str(result_dict))
print('Actual:   ' + str(create_email_dict(my_list)))
