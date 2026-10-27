# Name: 
# Email ID: 
import q2a
# The following dictionary is given.
gpa_dict = {'George Leung':3.4, 'Eric Wong':3.9, 'Michelle Lee': 3.1}

# --------------------------------------
# Write your code below:
print("Current GPA information: " + "\n")
q2a.display_all_gpas(gpa_dict)
print()

change = input("Whose GPA do you want to change? ")

while change not in gpa_dict:
    print("Sorry! This student doesn't exist." + "\n")

    change = input("Whose GPA do you want to change? ")

gpa_dict[change] = input("What's the new GPA? ")
print("Thanks! GPA has changed." + "\n")

print("The new GPA information: " + "\n")
q2a.display_all_gpas(gpa_dict)










