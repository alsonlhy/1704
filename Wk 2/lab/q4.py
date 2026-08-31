#Lab2_Q4
# #####################################
# Write your code below to first define 
# the function calculate_interest()

def calculate_interest(principal_amt, deposit_time):

    total_amt = principal_amt * (1 + ANNUAL_INTEREST_RATE/FREQUENCY_OF_COMPOUNDING)**(FREQUENCY_OF_COMPOUNDING*deposit_time)

    interest = total_amt - principal_amt

    rounded_interest = round(interest, 2)


    return rounded_interest





# ################################################################
# The default annual interest rate of 0.5%, compounded 
# monthly, has been provided for you.

# Annual interest rate (which is fixed)
ANNUAL_INTEREST_RATE = 0.005
# Number of times the interest is compounded per year
FREQUENCY_OF_COMPOUNDING = 12

# ################################################################
# Write your code below to prompt the user and display the 
# interest earned.

principal_amt = float(input("What is your principal amount? "))
deposit_time = float(input("How long is your deposit period? "))

interest_1 = calculate_interest(principal_amt, deposit_time)


print(interest_1)

