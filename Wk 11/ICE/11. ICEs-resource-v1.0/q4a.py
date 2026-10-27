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
        birthdate = column[2]
        new_dict[email] = birthdate

start = "Y"

while start == "Y":
    
    enter = input('Please enter an email ID: ')

    if enter not in new_dict:

        print("This is not a valid email ID.\n")
        
    else:
        print(f"The birthdate of this student is {new_dict[enter]}\n")
        
    
    start = input('Do you want to continue? [Y/N]: ')

    

print("Good-bye")
