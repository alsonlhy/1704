
# b) SOLUTION

is_student = input("Are you a student? ")

while not (is_student == "Yes" or is_student == "YES" or is_student == "yes" or is_student == "No" or is_student == "NO" or is_student == "no"):
    print("Please enter a valid answer (YES, Yes, yes, NO, No, no)")
    is_student = input("Are you a student? ")


print("Got it!")





