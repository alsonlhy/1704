import check_faculty

filename = 'facilities.txt'
# print(check_faculty(filename))

faculty = check_faculty.check_faculty(filename)
start = input("Do you want to search for the facilities within a school? [Y|N]: ")

while start != "N":

    search = input("Enter the school [LKCSB|SOE|SOL|SOA|SCIS]: ")
    print(f"The following facilities are in {search}:")
    print("Room #\tCap\tProjector?\n------\t---\t----------")
    selection = faculty[search]

    for rm, pax, proj in selection:
        print(rm + '\t' + str(pax) + '\t' + proj)

    start = input("Do you want to search for the facilities within a school? [Y|N]: ")


print("Good-bye!")  