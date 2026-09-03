## Q4
# PART 1
# The following function is for you to implement.
def get_ticket_info(age):
    
    # Modify the code below to return the right value
    
    if age < 3: 
        ticket_price = 0
        discount = True

    elif age <= 12:
        ticket_price = 22
        discount = True

    elif age < 60:
        ticket_price = 33
        discount = False

    else:
        ticket_price = 15
        discount = True

    return (ticket_price, discount)

    
    
# ################################################################################
# The code below is to test your implementation of the function above. 
# DO NOT MODIFY THE CODE BELOW!

# The following line of code should display (33, False)
# print(get_ticket_info(40))

# The following line of code should display (22, True)
# print(get_ticket_info(10))


# PART 2
# Write your code below to prompt the user for age
# and print the expected output

age = int(input("How old are you? "))

paying_price = get_ticket_info(age)

if paying_price[1] == True:
    print("Congratulations! You qualify for a discount.")
    print(f"You need to pay ${paying_price[0]}")

else:
    print(f"You need to pay ${paying_price[0]}")




