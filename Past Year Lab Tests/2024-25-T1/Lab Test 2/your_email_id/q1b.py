# Name:
# Email ID:

def alternate_and_reverse(s1, s2):

    new_str = ''

    len1 = len(s1)
    len2 = len(s2)

    for ch in s1:

        new_str += ch

        for ch2 in s2:

            new_str += ch2

    # if len1 > len2:
    #     num = len1-len2 
    #     new_str += len1[-1:num]

    # elif len2 > len1:
    #     num2 = len2 - len1
    #     new_str += len2[-1:num2]

    
    return new_str

