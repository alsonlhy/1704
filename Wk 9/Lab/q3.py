import random


gen_num = random.randint(1,100)
print(gen_num)

user_num = int(input("Enter your guess (between 1 and 100) :"))

while not (user_num == gen_num):

    if user_num < gen_num:

        print("Your guess is too low!")
        user_num = int(input("Enter your guess (between 1 and 100) :"))


    else:
        
        print("Your guess is too high!")
        user_num = int(input("Enter your guess (between 1 and 100) :"))


print("Bingo!")
