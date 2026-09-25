# Name:
# Email ID:

from q1a import compute_coe_rebate
from q1b import compute_parf_rebate

def get_highest_value(car_info_list):
    # Modify the code below.
    highest_dereg_value = 0
    name_of_highest_dereg = None
    
    for car in car_info_list:
        dereg_value = compute_coe_rebate(car) + compute_parf_rebate(car) 
        if dereg_value > highest_dereg_value:
            highest_dereg_value = dereg_value
            name_of_highest_dereg = car[0]
    return name_of_highest_dereg
    
