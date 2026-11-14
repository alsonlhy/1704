# Name:
# Email ID:
    
def find_people_in_range(people, bmr_range):

    names = ""
    count = 0
    for detail in people:
        name = detail[0]

        if detail[4] =="M":
            bmr = 10 * detail[1] + 6.25 * detail[2] - 5 * detail[3] + 5

        elif detail[4] == "F":
            bmr = 10 * detail[1] + 6.25 * detail[2] - 5 * detail[3] -161

        if bmr_range[0] <= bmr < bmr_range[1]:
            count += 1
            names += str(count) + "-" + name + "(" + str(int(bmr)) +")" + "-"



    
    return names[:-1]

