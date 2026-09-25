# Name:
# Email ID:

from q3a import manage_inventory

def process_orders(filename, list_of_orders):
    order_dict = {}
    
    inventory_dict = manage_inventory(filename)
    for order in list_of_orders:
        qty_filled = 0
        order_no, buyer, product, qty_ordered = order
        if product in inventory_dict:
            qty_in_stock = inventory_dict[product][0]
            if qty_in_stock >= qty_ordered:
                qty_filled = qty_ordered
                # update of the stock
                inventory_dict[product][0] -= qty_ordered
            else:
                qty_filled = qty_in_stock
                # update of the stock
                inventory_dict[product][0] = 0
            
        # update of order_dict
        if buyer not in order_dict:
            order_dict[buyer] = [ (order_no, product, qty_ordered, qty_filled) ]
        else:
            order_dict[buyer].append( (order_no, product, qty_ordered, qty_filled) )
    
    return order_dict