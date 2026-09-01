def get_discount_rate(num_boxes):
    
    if 2 <= num_boxes <= 4:
        disc_rate = 0.9
        return disc_rate


    elif num_boxes >= 5:
        disc_rate = 0.8
        return disc_rate

    else:
        disc_rate = 1
        return disc_rate


def calculate_total_amount(brand, num_boxes):

    if brand == "Tung Lok":
        price = 55.4
    

    elif brand == "Man Fu Yuan":
        price = 59.6

    total_amt = price * get_discount_rate(num_boxes) * num_boxes

    return total_amt

brand = input("Which brand do you want to buy?: ")
num_boxes = int(input("How many boxes do you want to buy?: "))

paying_cost = calculate_total_amount(brand, num_boxes)

print(f"You need to pay ${paying_cost:.2f}")

