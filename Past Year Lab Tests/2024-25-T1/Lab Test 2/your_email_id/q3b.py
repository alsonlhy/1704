# Name:
# Email ID:

def process_orders(filename, list_of_orders):

    inventory_dict = {}
    order_dict = {}
    with open (filename) as reading:

        for line in reading:
            line = line.rstrip("\n")
            columns = line.split(",")

            product_name = columns[0]
            category = columns[1]
            ppu = float(columns[2].lstrip("$"))
            cpu = float(columns[3].lstrip("$"))
            in_stock = int(columns[4])


            inventory_dict[product_name] = in_stock           

    for order in list_of_orders:
        order_id = order[0]
        buyer_name = order[1]
        product = order[2]
        qty_ordered = order[3]

        avail_stock = inventory_dict.get(product,0)

        if qty_ordered > avail_stock:
            qty_filled = avail_stock

        else:
            qty_filled = qty_ordered

        if buyer_name not in order_dict:
            order_dict[buyer_name] = [(order_id, product, qty_ordered, qty_filled)]

        else:
            existing_buyer = order_dict[buyer_name]
            existing_buyer.append((order_id, product, qty_ordered, qty_filled))


    return order_dict
