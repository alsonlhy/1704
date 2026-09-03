# Q5
# The following function is provided to you.
# Do not modify the function definition!
def get_user_info():
    """
    This function prompts the user for his/her name, gender, age and whether
    or not he/she is a student.
    The function returns a tuple that contains all the information entered
    by the user.
    """
    name = input("What's your name? ")
    gender = input("What's your gender? [M|F] ")
    age = int(input("What's your age? "))
    is_student = input("Are you a student? [yes|no] ")
    return (name, gender, age, is_student == 'yes')

# Write your code below:

info = get_user_info()

if info[2] <= 6:
    print(f"{info[0]}, you can travel for free.")

elif info[2] < 60:
    if info[1] == "M":
        gender = "Mr. "
    else:
        gender = "Mrs. "

    if info[3]:
        print(f"{gender}{info[0]}, you can get a concessionary fare for students.")

    else:
        print(f"{gender}{info[0]}, you need to pay full fare.")

else:
    if info[1] == "M":
        gender = "Mr. "
    else:
        gender = "Mrs. "

    print(f"{gender}{info[0]}, you can get a concessionary fare for senior citizens.")

