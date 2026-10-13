### Q1: Input Validation


age = int(input("Enter your age (btween 0 and 100, both inclusive): "))

while not (0 <= age <= 100):

    print("Please enter a valid age!")
    age = int(input("Enter your age again: "))

print("Thanks!")

