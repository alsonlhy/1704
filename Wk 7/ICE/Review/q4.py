def is_pangram(input_string):

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    input_string = input_string.lower

    for ch in alphabet:

        if ch not in input_string:

            return False
    
    return True

