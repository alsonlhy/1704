# Name:
# Email ID:

def compress(s):

    new_str = ""
    count = 0
    for i in range(len(s) -1):
        if s[i] == s[i+1]:
            count += 1
            new_str += s[i] + str(count)

        else:
            count = 0 


    
    return new_str
