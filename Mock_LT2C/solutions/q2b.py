# Mock LT2C - Q2 Part B (solution)
from q2a import read_trips


def get_spending(filename, card, mode=None):
    count = 0
    total = 0.0
    for trip_card, date, trip_mode, fare in read_trips(filename):
        if trip_card == card and (mode is None or trip_mode == mode):
            count += 1
            total += fare
    return (count, round(total, 2))       # (0, 0.0) falls out naturally when nothing matches
