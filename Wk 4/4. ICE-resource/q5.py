num_books = int(input("How many books do you have in your basket? "))

cost = 0

for i in range(num_books):
    price = float(input(f"What is the price of the book number {i+1}? "))
    cost += price
    books = [price]

avg = cost / num_books

print(f"Total price: ${cost:.2f}")
print(f"Average price: ${avg:.2f}")

print(books)


