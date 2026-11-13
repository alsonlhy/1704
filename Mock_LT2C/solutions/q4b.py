# Mock LT2C - Q4 Part B (solution)
from q4a import read_bookings


def to_hhmm(minutes):
    return f"{minutes // 60:02d}:{minutes % 60:02d}"


def get_rooms_needed(filename):
    bookings = read_bookings(filename)
    if bookings == []:
        return (0, None)
    best_count = 0
    best_time = None
    # The number of bookings in use can only go up at a start time,
    # so checking every start time is enough to find the maximum.
    for _, _, t, _ in bookings:
        in_use = 0
        for _, _, start, end in bookings:
            if start <= t < end:                       # end time is exclusive
                in_use += 1
        if in_use > best_count or (in_use == best_count and t < best_time):
            best_count = in_use
            best_time = t
    return (best_count, to_hhmm(best_time))
