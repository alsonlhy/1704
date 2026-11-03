def find_last_letter(my_str):

    if my_str == "":
        return (-1)

    count = 0
    check_letter = False

    for char in my_str:
        if char.isalpha():
            check_letter = True
            count += 1

        else: 
            check_letter = False
            count += 1

    return count
    