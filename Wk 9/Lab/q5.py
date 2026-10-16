def check_strings(string1, string2):

    if " " in string1 or " " in string2:

        return False

    if len(string2) <= len(string1):

        return False

    for ch in string1:

        if ch not in string2:

            return False

    return True


string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

while not (check_strings(string1, string2)):

    print("Conditions not satisfied!")
    string1 = input("Enter the first string: ")
    string2 = input("Enter the second string: ")

print("Bingo!")
    
