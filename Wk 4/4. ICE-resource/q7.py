
# Q7
import string
has_lower = False
has_upper = False
has_digit = False
has_symbol = False

s = input('Input a password: ')
if len(s) < 8:
    print(False)
else:
    for i in s:
        if i in '!@#$':
            has_symbol = True
        if i in string.digits:
            has_digit = True
        if i in string.ascii_lowercase:
            has_lower = True
        if i in string.ascii_uppercase:
            has_upper = True
    
    if has_lower and has_upper and has_digit and has_symbol:
        print(True)
    else:
        print(False)
    


