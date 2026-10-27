# Name: 
# Email ID: 

def display_all_gpas(gpa_dict):
    print("Student Name" + "\t" + "Student GPA")
    print("-" *10 + "\t" + "-"*10)

    for key in gpa_dict:
        print(f"{key}{"\t"}{gpa_dict[key]}")


