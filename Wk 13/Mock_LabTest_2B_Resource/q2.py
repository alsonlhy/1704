def check_age(student_list):
    # check = 1

    # for tup in student_list:

    #     if tup[1] == "M" and int(tup[2]) > 20:
    #         check = 1
            
    #     else:
    #         check = 0


    # if check == 1:
    #     return True
    # else:
    #     return False


    for tup in student_list:

        if tup[1] == "M" and int(tup[2]) <= 20:
            return False

    return True

   
