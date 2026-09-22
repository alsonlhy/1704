# Name:
# Email ID:

def check_numbers(int_list_1 ,int_list_2):

    for num1 in int_list_1:

        checker = False

        for num2 in int_list_2:
            if num1 % num2 == 0:
                checker = True

        if not checker:
            return False

    return True   

