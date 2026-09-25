# Name:
# Email ID:


def compute_coe_rebate(car_info):
    # Modify the code below.
    car_name, num_days_as_owner, coe_arf_list = car_info
    coe_paid = float(coe_arf_list[0][1:])
    number_days_left = 10 * 365 - num_days_as_owner
    coe_rebate = coe_paid * number_days_left / (10 * 365)
    
    return int(coe_rebate)
    