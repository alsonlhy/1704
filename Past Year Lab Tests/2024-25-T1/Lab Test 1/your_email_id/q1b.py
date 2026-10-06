# Name:
# Email ID:

def is_allowed_in_carryon(item_category, quantity):

    is_allowed = False

    approved_items = ["Electronics", "Liquids", "Food"]

    if item_category in approved_items:

        is_allowed = True

        if item_category == approved_items[1] and quantity > 100:
            is_allowed = False

    elif item_category == "Weapons":
        is_allowed = False

    else:
        return "Contact Staff"
    
    return is_allowed

    
