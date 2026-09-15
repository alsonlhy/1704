## Q1 Initials
# Write your code below:
##############################


num_attendees = int(input("How many people will attend the meeting? "))

attendee_list = []

for i in range(num_attendees):
    name = input(f"Participant {i+1}: ")
    attendee_list.append(name)


for element in attendee_list:

    name_split = element.split(' ')

    for i in range(len(name_split)):
    
        print(element.split(' ')[i][0], end="")

    print()



