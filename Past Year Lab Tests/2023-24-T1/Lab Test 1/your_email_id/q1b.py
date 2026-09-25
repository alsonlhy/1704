# Name:
# Email ID:

def compute_rebate(is_singaporean_household, flat_type, month):

    if is_singaporean_household:

        if flat_type in ("1", "2"):

            if month == 1:
                return 0.5

            elif month in (4,7,10):
                return 1.0

            else:
                return 0.0
            
            

        elif flat_type in ("3", "4"):

            if month in (1,7,10):
                return 0.5

            elif month == 4:
                return 1.0

            else:
                return 0.0

            

        elif flat_type == "5":

            if month in (1,4,7,10):

                return 0.5

            else:
                return 0.0

        
        elif flat_type == "E":

            if month == 1:
                return 0.0

            elif month in (4,7,10):
                return 0.5

            else:
                return 0.0

            

    else: 
        return 0.0



    