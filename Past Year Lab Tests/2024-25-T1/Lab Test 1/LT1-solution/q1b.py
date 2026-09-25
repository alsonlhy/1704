# Name:
# Email ID:

def is_allowed_in_carryon(item_category, quantity):
    # Replace the code below with your implementation.
    if item_category == "Electronics" or item_category == "Food":
        return True
    elif item_category == "Weapons":
        return False
    elif item_category == "Liquids":
        if quantity <= 100:
            return True
        else:
            return False
    else:
        return "Contact Staff"

    
