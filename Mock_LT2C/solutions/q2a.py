# Mock LT2C - Q2 Part A (solution)

def read_trips(filename):
    trips = []
    with open(filename) as f:
        f.readline()                       # skip the header line
        for line in f:
            line = line.rstrip('\n')
            if line == '':
                continue
            card, date, mode, fare = line.split('|')
            year, month, day = date.split('-')
            trips.append((card, (int(year), int(month), int(day)), mode, float(fare.lstrip('$'))))
    return trips
