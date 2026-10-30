with open("employees.txt") as reading:

    em_dict = {}

    for line in reading:

        line = line.rstrip("\n")
        keyvalue = line.split("\t")


        id = int(keyvalue[0].split(":")[1])
        em_dict[id] = keyvalue[1:]

    print(em_dict)


em_id = int(input("Enter an employee ID: "))

picklist = em_dict[em_id]

for item in picklist:
    inner_dict = {}
    newkeyvalue = item.split(":")
    inner_dict[newkeyvalue[0]] = newkeyvalue[1]

print(inner_dict)



    