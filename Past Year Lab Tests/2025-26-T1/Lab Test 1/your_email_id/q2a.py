# Name:
# Email ID:
    
def calculate_bmr(weight, height, age, gender):
    
    if gender == "M":

        bmr = 10 * weight + 6.25 * height - 5 * age + 5

    elif gender == "F":

        bmr = 10 * weight + 6.25 * height - 5 * age - 161

    
    return int(bmr)
