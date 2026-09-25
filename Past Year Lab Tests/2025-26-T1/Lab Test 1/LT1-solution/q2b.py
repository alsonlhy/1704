# Name:
# Email ID:

import q2a
    
def find_people_in_range(people, bmr_range):
    # Modify the code below.
    min_bmr = bmr_range[0]
    max_bmr = bmr_range[1]
    index = 1
    str_to_return = ''
    
    for name, weight, height, age, gender in people:
        bmr = q2a.calculate_bmr(weight,height,age,gender)
        if bmr < max_bmr and bmr >= min_bmr:
            str_to_return += str(index) + "-" + name + "(" + str(bmr) + ")" + "-"
            index += 1
    
    if str_to_return != "":
        str_to_return = str_to_return[:-1]

    return str_to_return

