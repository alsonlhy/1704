# Name:
# Email ID:

def compute_parf_rebate(car_info):
    # Modify the code below.
    car_name, num_days_as_owner, coe_arf_list = car_info
    arf_paid = float(coe_arf_list[1][1:])
    
    parf_percent = 0
    if num_days_as_owner <= 5 * 365:
        parf_percent = 0.75
    elif num_days_as_owner <= 6 * 365:
        parf_percent = 0.70
    elif num_days_as_owner <= 7 * 365:
        parf_percent = 0.65
    elif num_days_as_owner <= 8 * 365:
        parf_percent = 0.60
    elif num_days_as_owner <= 9 * 365:
        parf_percent = 0.55
    else:
        parf_percent = 0.50
    
    parf_rebate = arf_paid * parf_percent
    
    return int(parf_rebate)
