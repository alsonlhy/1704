
### Q2: Integers

integer = int(input("Enter an integer: "))
new_string = ""

while not(integer < 0):
    if integer %2 != 0:
        new_string += str(integer) + ", "

    integer = int(input("Enter an integer: "))

print("Thanks")
print(f"The odd positive integers you have entered are the following: {new_string[:-2]}")
