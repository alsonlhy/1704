# Name:
# Email ID:
    
def is_food_safe(temp, holding_time):
    # Modify the code below.
    if temp >= 75 and temp <= 100:
        return True
    elif temp >= 60 and temp < 75 and holding_time >= 2:
        return True
    else:
        return False