# Name: 
# Email ID: 

book_author_dict = {"Harry Potter and the Sorcerer's Stone":'J.K. Rowling', 
               "Turtles All the Way Down":'John Green',
               "Animal Farm and 1984":'George Orwell',
               "The Da Vinci Code":'Dan Brown',
               "Harry Potter and the Goblet of Fire":'J.K. Rowling',
               "Origin":'Dan Brown'}

# -----------------------
# Write your code below

search = input("Do you want to search for the author of a book? [Y/N]")

while search != "N":

    title = input("Please enter a book title: ")
    if title in book_author_dict:
        print(book_author_dict[title])
    else:
        print("Not found!")

    search = input("Do you want to continue? [Y/N]")

print("Good-bye!")




