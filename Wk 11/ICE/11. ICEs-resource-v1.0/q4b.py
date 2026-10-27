# Name: 
# Email ID: 

#--------------------------------
# Write your code below

# Name: 
# Email ID: 

#--------------------------------
# Write your code below

new_dict = {}

with open('students.txt') as reading:

    for line in reading:

        line = line.rstrip("\n")
        column = line.split("\t")

        email = column[1]
        data = (column[0], column[3], column[2])
        new_dict[email] = data
        

start = "Y"

while start == "Y":
    
    enter = input('Please enter an email ID: ')

    if enter not in new_dict:

        print("This is not a valid email ID.\n")
        
    else:

        if new_dict[enter][1] == "M":
            gender = "Male"

        else: gender = "Female"

        print(f"The birthdate of this student is {new_dict[enter][0]}, {gender}, born on {new_dict[enter][2]}\n")
        
    
    start = input('Do you want to continue? [Y/N]: ')
