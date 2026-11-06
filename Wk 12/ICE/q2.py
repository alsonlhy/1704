
# ### Q2: Count Strings

# write your code below

# create dict for letter to upper and lowercase
count_dict = {}

# accept input of string
new_input = input("Enter a string > ").lower()

# lowercase the input

# create counter for cumulative sum 

while new_input != "":
    count = 1
    if new_input[0] not in count_dict:
        count_dict[new_input[0]] = (1, new_input[0].upper(), new_input[0])

    else:
        count += 1
        count_dict[new_input[0]] = (count, new_input[0].upper(), new_input[0])

    new_input = input("Enter a string > ").lower()

print("\nYou've entered")
# exit while loop: if > 1 then strings

for key in count_dict:
    amt = count_dict[key]
    if amt[0] > 1:
        if amt[1].isalpha():
            print(f"\t{amt[0]} strings starting with '{amt[1]}' or '{amt[2]}'")
        else:
            print(f"\t{amt[0]} strings starting with '{amt[1]}'")


    else: 
        if amt[1].isalpha():
            print(f"\t{amt[0]} string starting with '{amt[1]}' or '{amt[2]}'")
        else:
            print(f"\t{amt[0]} string starting with '{amt[1]}'")