# Name:
# Email ID:
    
def is_food_safe(temp, holding_time):

    if 75 <= temp <= 100:
        return True

    elif 60 <= temp <75:
        if holding_time >= 2:
            return True
        else:
            return False

    else:
        return False
    
    
