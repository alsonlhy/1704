# Name: 
# Email ID: 

#--------------------------------
# Write your code below

phonebook = {}

with open('phone_numbers.txt') as reading:

    for line in reading:

        line = line.rstrip("\n")
        person, number = line.split("|")

        if person not in phonebook:
            phonebook[person] = [number]

        else:
            existing = phonebook[person]
            existing.append(number)


name = input("Enter a person's name: ")

if name in phonebook:

    nums = phonebook[name]


    print(f'{name} has {len(nums)} number(s): ')
    for num in nums:
        print(num)
    print()

else:
    print(f"{name} cannot be found in our database")


