def check_room(filename):

    sch_dict = {}

    with open(filename) as reading:

        for line in reading:

            line = line.rstrip("\n")
            sch, rm, pax, proj = line.split("\t")


            sch_dict[sch,rm] = [pax, proj]


    return sch_dict


filename = 'facilities.txt'
# print(check_room(filename))

sch_dict = check_room(filename)
start = input("Do you want to search for a facility? [Y/N]: ")

while start != "N":

    sch = input("Enter the school [LKCSB|SOE|SOL|SOA|SCIS]: ")
    room = input("Enter the room number: ")

    pax = sch_dict[sch, room][0]
    if sch_dict[sch, room][1] == "yes":
        proj = "has a projector"

    else:
        proj = "does not have a projector"

    print(f"{sch} {room} has a capacity of {pax} and {proj}.")

    start = input("Do you want to continue the search? [Y|N]: ")

print("Thanks for using our system!")
