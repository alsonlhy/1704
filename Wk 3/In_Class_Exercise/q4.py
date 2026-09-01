def calculate_tax_4(income):

    if income <= 20000:
        tax = 0

    elif income <= 30000:
        tax = 0.02 * (income - 20000)

    elif income <= 40000:
        tax = 0.035 * (income - 30000) + 200

    elif income <= 80000:
        tax = 0.07 * (income - 40000) + 550

    elif income <= 120000:
        tax = 0.115 * (income - 80000) + 3350

    return tax

revenue = float(input("Enter your annual income: "))

print(f"\nYour tax is ${calculate_tax_4(revenue):.2f}\n")