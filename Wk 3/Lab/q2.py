## Q2 PART 1
# These variables are defined for you to use.
MEMBER_DISCOUNT_RATE = 0.10
SALE_ITEM_DISCOUNT_RATE = 0.05

# This function is for you to implement!
def calculate_price(orig_price, is_member, is_on_sale):
    
    # ################################################################################
    # Modify the code below to return the correct discounted price.
    if is_member == "Yes":

        if is_on_sale == "Yes":
           disc_price = orig_price * (1 - 0.15)

        else:
            disc_price = orig_price * (1 - 0.10)

    elif is_member == "No":
        if is_on_sale == "Yes":
            disc_price = orig_price * (1 - 0.95)

        else:
            return orig_price

    return disc_price
    # ################################################################################

## Q2 PART 2
# Write your code below to prompt the user for the following information: 
# (1) The original price of the item. 
# (2) Whether the user is a member or not. 
# (3) Whether the item is on sale or not.:

orig_price = float(input("What's the original price of the item: "))
is_member = input("Are you a member [Yes | No]? ")
is_on_sale = input("Is the item on sale [Yes | No]? ")

final_price = calculate_price(orig_price, is_member, is_on_sale)

print(f"The final price of the item is {final_price}")
