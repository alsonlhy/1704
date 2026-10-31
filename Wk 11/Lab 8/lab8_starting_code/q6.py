em_dict = {}

with open("employees.txt") as reading:
    for line in reading:
        line = line.rstrip("\n")
        keyvalue = line.split("\t")

        # Extract the employee id as an integer
        emp_id = int(keyvalue[0].split(":")[1])

        # Build the inner dictionary for this specific employee
        inner_dict = {}
        for item in keyvalue[1:]:
            key, val = item.split(":")
            inner_dict[key] = val

        em_dict[emp_id] = inner_dict

resume_search = "Y"

while resume_search != "N":
    user_id = int(input("Enter an employee ID: "))

    if user_id in em_dict:
        em_info = em_dict[user_id]
        print(f"This employee is {em_info.get('name')}.")

        check_field = input("    Enter a field name or 'S' to stop: ")
        while check_field != "S":
            if check_field in em_info:
                print(f"    The {check_field} is {em_info[check_field]}.")
            else:
                print("    Not found!")
            # Prompt again to avoid an infinite loop
            check_field = input("    Enter a field name or 'S' to stop: ")

    else:
        print("Not found!")

    # Prompt again to avoid an infinite outer loop
    resume_search = input(
        "\nDo you want to search for another employee? [Y|N]: "
    )

print("\nGood-bye!")