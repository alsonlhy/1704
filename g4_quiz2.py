def separate_letters(text):

    upper_letters = ""
    lower_letters = ""

    for ch in text:

        if ch.isupper():
            upper_letters += ch

        elif ch.islower():
            lower_letters += ch

    return (upper_letters, lower_letters)


def display_balance(text):

    tup = separate_letters(text)

    print(tup)

    if len(tup[0]) == len(tup[1]):
        print("Balanced")

    else: 
        print("Not balanced")


display_balance("PyTHon3")
display_balance("Good Day!!")