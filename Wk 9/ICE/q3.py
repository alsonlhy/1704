
### Q3: Voucher
voucher = 100
total_price = 0

book_price = float(input("Please pick a book. How much is it (in $)? "))
total_price += book_price
voucher -= book_price

while voucher > 0:

    print(f"You still have ${voucher} left.")
    book_price = float(input("Please pick another book. How much is it (in $)? "))
    total_price += book_price
    voucher -= book_price

print("You are done!")
print(f"The total price is ${total_price}")
