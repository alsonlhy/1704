# Name:
# Email ID:

def get_entry_count(filename, swimmer_name = None):

    count = 0
    swimmers = []
    with open (filename) as reading:

        count_line = 0
        for line in reading:
            line = line.rstrip("\n")
            columns = line.split(",")

            name = columns[0]
            swimmers.append(name)

        if swimmer_name == None:
            return len(swimmers)
        
        for swimmer in swimmers:

            if swimmer_name == swimmer:
                count += 1
        return count
        

	
