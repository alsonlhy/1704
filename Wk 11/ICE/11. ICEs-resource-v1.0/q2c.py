# Name: 
# Email ID: 
import q2a
# The following dictionary is given.
gpa_dict = {'George Leung':3.4, 'Eric Wong':3.9, 'Michelle Lee':3.1}

#-------------------------------------------------------------------
# Write your code below

print("Current GPA information: " + "\n")
q2a.display_all_gpas(gpa_dict)
print()

change = input("Whose GPA do you want to add? ")

while change in gpa_dict:
    print("Sorry! This student already exists." + "\n")

    change = input("Whose GPA do you want to add? ")

gpa_dict[change] = input(f"What's the GPA of {change}? ")
print("Thanks! GPA has been added" + "\n")

print("The new GPA Information: ")
q2a.display_all_gpas(gpa_dict)