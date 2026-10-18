cart = input("Do you have any item left in your shopping cart? Please enter Y or N: ")
total = 0
summary = []

while not (cart == "N"):

    item = input("Please enter the name of the item: ")
    price = float(input("Please enter the price of the item: "))
    qty = int(input("Please enter the quantity of the item: "))
    total += price * qty
    summary.append((item, price, qty))

    cart = input("\nDo you have any item left in your shopping cart? Please enter Y or N: ")


print("You have entered the following items: ")
for item_name, item_price, item_qty in summary:
    print(f"{item_name}\t{item_price}\t{item_qty}")


print(f"\nTotal price: ${total}")