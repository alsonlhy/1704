# Name:
# Email ID:

def compute_parking(duration):

    if duration <= 10:

        cost = 0.0

    elif duration < 60:

        cost = 5.0

    else: 
        cost = 5.0 + (duration - 60) * 0.1

    
    return cost