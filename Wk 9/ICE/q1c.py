
# c) SOLUTION
# check if a string is a valid name

def check_string(name):

    approved_strings = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']

    for ch in name:

        if ch not in approved_strings:
            return False


    return True


name = str(input("Enter your name: "))

while not check_string(name):
    print("Please enter a valid name! ")
    name = str(input("Enter your name: "))

print("Thank you!")