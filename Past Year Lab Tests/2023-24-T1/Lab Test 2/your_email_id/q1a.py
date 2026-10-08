# Name:
# Email ID:


def compute_coe_rebate(car_info):

    coe_paid = int(car_info[2][0][1:])
    days_left = 3650 - car_info[1]

    rebate = coe_paid * days_left / (3650)


    
    return int(rebate)



