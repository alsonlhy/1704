# Name:
# Email ID:

def convert_to_int_float_or_string(x):
    if x == '':         # Empty values -> None
        return None
    if x.isdigit():     # All-digit strings -> int
        return int(x)
    # All-digit strings with one decimal -> float
    # Note: the Pythonic way of strings-float conversion
    # involves try/except. This code uses IS111 concepts.
    ix = x.find('.')
    if ix != -1 and x[0:ix].isdigit() and x[ix+1:].isdigit():
        return float(x)
    return x            # All others are strings

def load_pokedex(filename):
    with open(filename, 'r') as fp:
        hdr = fp.readline()            # Read header line
        keys = hdr.rstrip().split(',') # Get dict keys / field names
        lst = []
        # Body of CSV is data
        for line in fp:
            line = line.rstrip()
            x = {}
            line = line.split(',')
            # Assign header name as the key for each field
            # This solution uses IS111 concepts
            for ix in range(len(keys)):                
                x[keys[ix]] = convert_to_int_float_or_string(line[ix])
            lst.append(x)
    return lst