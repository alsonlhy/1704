## Q2
# ################################################################################
# The following code is provided to you. DO NOT MODIFY THE CODE!

import random
num1 = random.randrange(0, 10) 
num2 = random.randrange(0, 10)
num3 = random.randrange(0, 10)

print('*****************')
print('**', num1, '**', num2, '**', num3,'**')
print('*****************')

# ################################################################################
# Write your code here:

if num1 == num2 and num2 == num3:
    print("Jackpot!")

elif num1 == num2 or num2 == num3 or num1 == num3:
    print("Two of a kind!")

else:
    print("Try again!")
