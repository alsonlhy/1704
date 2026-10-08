# Name:
# Email ID:

def compute_parf_rebate(car_info):

    arf_paid = int(car_info[2][1][1:])

    if car_info[1] / 365 <= 5:
        parf_percent = 0.75

    elif car_info[1] / 365 <= 6:
        parf_percent = 0.7

    elif car_info[1] / 365 <= 7:
        parf_percent = 0.65

    elif car_info[1] / 365 <= 8:
        parf_percent = 0.6

    elif car_info[1] / 365 <= 9:
        parf_percent = 0.55

    elif car_info[1] / 365 <= 10:
        parf_percent = 0.5

    parf_rebate = arf_paid * parf_percent

    
    return int(parf_rebate)

