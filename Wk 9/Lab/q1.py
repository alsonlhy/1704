gender = input("What's your gender? Please enter M or F: ")

while not (gender == "M" or gender == "F"):

    print("Wrong input!")
    gender = input("What's your gender? Please enter M or F: ")


if gender == "M":

    gen = "Male"

else:
    gen = "Female"

print(f"Thanks! Your gender is {gen}")