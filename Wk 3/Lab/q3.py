## Q3 PART 1
# This function is for you to implement!
def calculate_salary(monthly_sales):
    
    # This variable is defined for you to use.
    BASE_SALARY = 2000.0
    
    # ################################################################################
    # Modify the code below to return the right amount of salary.
    if monthly_sales < 10000:
        commission = 0.05 * monthly_sales

    elif monthly_sales < 15000:
        commission = 0.1 * monthly_sales

    elif monthly_sales < 18000:
        commission = 0.15 * monthly_sales

    else:
        commission = 0.18 * monthly_sales
    
    return commission + BASE_SALARY
    # ################################################################################

## Q3 PART 2
# Write your code below

monthly_sales = float(input("Enter monthly sales amount ($): "))

monthly_salary = calculate_salary(monthly_sales)

print(f"The monthly pay for the salesperson is ${monthly_salary:.2f}")

