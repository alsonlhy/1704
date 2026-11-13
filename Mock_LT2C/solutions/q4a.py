# Mock LT2C - Q4 Part A (solution)

def to_minutes(hhmm):
    hours, minutes = hhmm.split(':')
    return int(hours) * 60 + int(minutes)


def read_bookings(filename):
    bookings = []
    with open(filename) as f:
        for line in f:
            line = line.rstrip('\n')
            if line == '':
                continue
            booking_id, room, start, end = line.split(',')
            bookings.append((booking_id, room, to_minutes(start), to_minutes(end)))
    return bookings


def get_clashes(filename):
    bookings = read_bookings(filename)
    clashes = []
    for i in range(len(bookings)):
        for j in range(i + 1, len(bookings)):          # every pair once, earlier one first
            id_a, room_a, start_a, end_a = bookings[i]
            id_b, room_b, start_b, end_b = bookings[j]
            if room_a == room_b and start_a < end_b and start_b < end_a:
                clashes.append((id_a, id_b))
    return clashes
