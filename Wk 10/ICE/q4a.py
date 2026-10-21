# Name: 
# Email ID:

# Write your code below:

keyword = input("Enter a  keyword or a keyphrase: ")
keyword = keyword.lower()

count = 0

with open('news.txt') as reading:


    for line in reading:

        line = line.rstrip('\n')
        if keyword in line.lower():

            count += 1
            print(f"{count}. {line}")