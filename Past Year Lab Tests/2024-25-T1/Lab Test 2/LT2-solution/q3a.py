# Name:
# Email ID:

def calculate_profit_margin(selling_price, buying_price):
    return (selling_price - buying_price) / buying_price

def calculate_min_stock(profit_margin):
    if profit_margin >= 0.5:
        return 3
    elif 0.2 <= profit_margin < 0.5:
        return 8
    else:
        return 15
    
def clean_price(price_str):
    if price_str[0] == '$':
        return float(price_str[1:])
    else:
        return float(price_str)
    
def manage_inventory(filename):
    # Replace the code below with your implementation.
    
    inventory_dict = {}
    with open(filename, 'r') as my_file:
        for line in my_file:
            line = line.strip('\n')
            product, category, selling_price_str, buying_price_str, qty_str = line.split(',')
            selling_price = clean_price(selling_price_str)
            buying_price = clean_price(buying_price_str)
            qty = int(qty_str)
            profit_margin = calculate_profit_margin(selling_price, buying_price)
            min_stock = calculate_min_stock(profit_margin)
            inventory_dict[product] = [qty, min_stock]
    
    return inventory_dict