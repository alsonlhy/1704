# Lab2_Q5
# ########################################
# # lab2_Q5_part1: Write your code below:

def calculate_price_after_discount(unit_price, quantity, discount):
    final_price = unit_price * quantity * (1-discount/100)

    return final_price




x = calculate_price_after_discount(1.5, 5, 10)
print(x)





# ########################################
# lab2_Q5_part2: Write your code below:

milk = calculate_price_after_discount(5.95, 2, 10)
rice = calculate_price_after_discount(6.5, 1, 5)
eggs = calculate_price_after_discount(2.4, 2, 0)
kaya = calculate_price_after_discount(3.95, 3, 15)

total = milk + rice + eggs + kaya

print(f"The total of your shopping cart after discount is ${total:.2f}")




