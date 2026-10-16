import random

practice = input("Do you want to practice multiplication table? Please enter Y or N: ")


while not (practice == "N" or practice =="n"):

    num1 = random.randint(1,9)
    num2 = random.randint(1,9)

    answer = num1 * num2

    user_ans = int(input(f"What's the result of {num1} times {num2}? "))

    while not (user_ans == answer):

        user_ans = int(input(f"Wrong answer! Please try again: "))

    print("You are right!")
    practice = input("Do you want to continue your practice? Please enter Y or N: ")


print("Good-bye!")

