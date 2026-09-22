# =====
# q2.py
# =====
# Name: 
# Email ID:

def add_first_odd_digits(str_list):

    total = 0

    for string in str_list:

        for ch in string:
            if ch.isdigit() and int(ch) % 2 != 0:

                total += int(ch)

                break

            

            

    
    return total
