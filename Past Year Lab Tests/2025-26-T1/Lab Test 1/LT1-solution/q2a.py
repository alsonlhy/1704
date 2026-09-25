# Name:
# Email ID:
    
def calculate_bmr(weight, height, age, gender):
    # Modify the code below.
    if gender == 'M':
        return int(10 * weight + 6.25 * height - 5 * age + 5)
    else:
        return int(10 * weight + 6.25 * height - 5 * age - 161)
