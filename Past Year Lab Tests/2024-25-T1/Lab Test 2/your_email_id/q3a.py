# Name:
# Email ID:

def manage_inventory(filename):

    inventory_dict = {}
    with open (filename) as reading:

        for line in reading:
            line = line.rstrip("\n")
            columns = line.split(",")

            product_name = columns[0]
            category = columns[1]
            ppu = float(columns[2].lstrip("$"))
            cpu = float(columns[3].lstrip("$"))
            in_stock = int(columns[4])

            prof_margin = (ppu-cpu) / cpu

            if prof_margin >= 0.5:
                min_stock = 3
            elif prof_margin >= 0.2:
                min_stock = 8
            else:
                min_stock = 15

            inventory_dict[product_name] = [in_stock, min_stock]
    
    return inventory_dict
