# Name:
# Email ID:

from q1a import compute_coe_rebate
from q1b import compute_parf_rebate

def get_highest_value(car_info_list):

    highest_value = 0
    most_value_car = ""

    for car in car_info_list:

        coe_rebate = compute_coe_rebate(car)
        parf_rebate = compute_parf_rebate(car)

        total = coe_rebate + parf_rebate

        if total > highest_value:

            highest_value = total
            most_value_car = car[0]



    return most_value_car
