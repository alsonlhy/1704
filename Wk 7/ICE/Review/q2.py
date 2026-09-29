def transform_string(input_string):

    upper_count = 0
    lower_count = 0
    digits_count = 0
    symbols_count = 0
    new_string = ''

    for ch in input_string:

        if ch.isupper():
            new_string = new_string + 'L'
            upper_count += 1

        elif ch.islower():
            new_string = new_string + 'l'
            lower_count += 1

        elif ch.isdigit():
            new_string = new_string + 'd'
            digits_count += 1

        else:
            new_string = new_string + 's'
            symbols_count += 1


    print(f"Number of uppercase letters: {upper_count}")
    print(f"Number of lowercase letters: {lower_count}")
    print(f"Number of digits: {digits_count}")
    print(f"Number of symbols: {symbols_count}")

    return new_string

print(transform_string("IS1704 is a fun module"))