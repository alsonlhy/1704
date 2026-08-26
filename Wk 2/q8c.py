# ################################################################################
# This function is for you to implement!
def calculate_tax_3(income):
    """
    This function assumes that the income is between $0 and $40,000.
    """
    
    # Modify the code below to return the right amount of tax.
    tax1 = max(0, income - 20000) * 0.02
    tax2 = max(0, income - 30000) * 0.015
    tax3 = max(0, income - 40000) * 0.035
    tax4 = max(0, income - 80000) * 0.045

    total_tax = tax1 + tax2 + tax3 + tax4
    return total_tax



# ################################################################################

# Call the function above to test whether it works.
print(calculate_tax_3(25000.0))
print(calculate_tax_3(10000.0))
print(calculate_tax_3(35000.0))
print(calculate_tax_3(45000.0))
print(calculate_tax_3(95000.0))

# ################################################################################
