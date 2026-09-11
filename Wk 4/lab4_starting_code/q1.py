month = int(input("Enter month: "))

if month not in range (1,13):
    print("Enter a number between 1 and 12 only!")

elif month == 2:
    print("There are 28 days in this month.")

elif month in (4,6,9,11):
    print("There are 30 days in this month.")

else:
    print("There are 31 days in this month.")

