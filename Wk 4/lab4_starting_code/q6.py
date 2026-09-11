## Q6
######################################################################################
# This code is provided to you. DO NOT MODIFY THE CODE!
def calculate_price_after_discount(unit_price, quantity, discount_rate):
    """
    This function takes in the unit price, quantity and discount rate of an item.
    It returns the total price after discount for the item.
    Parameters:
        - unit_price (float): The unit price of the item.
        - quantity (int): The quantity of the item being purchased.
        - discount_rate (float): The percentage of discount. E.g., if there's a 
          10% discount, then discount_rate is set to 10.
    Return:
        - The total price of the item with the specified quantity after discount.
    """
    return (unit_price * quantity * (1 - discount_rate/100))

######################################################################################
# Write your solution below for Part A:
# num_of_items = int(input("How many items do you want to check out? "))

total_price = 0

for i in range(num_of_items):
    print(f"Enter the details of Item {i+1}")
    item = input("What's this item? ")
    price = float(input("What's the unit price of this item? "))
    qty = int(input("What's the quantity of this item? "))
    disc = input("Does this item have any discount? [yes/no] ")

    if disc == 'yes':
        percent_disc = float(input("What's the percentage of discount (%)? "))
        total_price += calculate_price_after_discount(price, qty, percent_disc)

    else:
        total_price += price * qty

print(f"The total amount you have to pay is ${total_price:.2f}")




######################################################################################
# Write your solution below for Part B:
def calculate_price_after_discount2(unit_price, quantity, discount_rate):

    discounted_price = unit_price * quantity * (1 - discount_rate/100)
    amount_saved = unit_price * quantity - discounted_price

    return (discounted_price, amount_saved)


num_of_items = int(input("How many items do you want to check out? "))

total_price = 0
saved = 0

for i in range(num_of_items):
    print(f"Enter the details of Item {i+1}")
    item = input("What's this item? ")
    price = float(input("What's the unit price of this item? "))
    qty = int(input("What's the quantity of this item? "))
    disc = input("Does this item have any discount? [yes/no] ")

    if disc == 'yes':
        percent_disc = float(input("What's the percentage of discount (%)? "))
        discounted_price, amount_saved = calculate_price_after_discount2(price, qty, percent_disc)
        total_price += discounted_price
        saved += amount_saved

    else:
        total_price += price * qty


print(f"The total amount you have to pay is ${total_price:.2f}")
print(f"You have saved ${saved:.2f}")


