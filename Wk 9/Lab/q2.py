num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number:"))


while not((num1 > 0 and num2 > 0) and (num1 + num2)<100):

    print("Conditions not satisfied!")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number:"))



print("Thanks!")