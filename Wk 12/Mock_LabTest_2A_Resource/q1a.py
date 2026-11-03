def find_last_letter(my_str):


    for i in range(len(my_str)-1, -1, -1):
        ch = my_str[i]
        if ch.isalpha():
            return i 
    
    return (-1)


    