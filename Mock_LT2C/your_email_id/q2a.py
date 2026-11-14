# Name:
# Email ID:

def read_trips(filename):
    """
    Return a list of (card, (year, month, day), mode, fare) tuples.
    """
    return_list = []
    with open (filename) as reading:
        reading.readline()

        for line in reading:
            line = line.rstrip("\n")
            columns = line.split("|")

            card = columns[0]
            year = int(columns[1].split("-")[0])
            month = int(columns[1].split("-")[1])
            day = int(columns[1].split("-")[2])
            mode = columns[2]
            fare = float(columns[3].lstrip("$"))

            return_list.append((card, (year,month,day),mode,fare))


        
    return return_list
