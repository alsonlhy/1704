gender = input("What's your gender? Please enter M or F: ")

while not (gender == "M" or gender == "F"):

    print("Wrong input!")
    gender = input("What's your gender? Please enter M or F: ")


if gender == "M":

    gen = "male"

else:
    gen = "female"

print(f"Thanks! Your gender is {gen}")