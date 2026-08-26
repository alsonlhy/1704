import week2_utility

age = int(input("What is your age: "))
gender = input("What is your gender (M/F): ")

price = week2_utility.get_insurance_premium(age, gender)

print(price)