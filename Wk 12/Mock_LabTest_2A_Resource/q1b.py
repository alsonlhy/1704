def find_second_letter(my_str):

    overall_count = 0
    letter_count = 0

    for char in my_str:

        if char.isalpha() == False:

            overall_count += 1

        else: 
            letter_count += 1
            overall_count += 1

        if letter_count == 1:

            return overall_count
        
        elif my_str == "" or letter_count == 0:
        
            return (-1)

        


