# Name:
# Email ID:

# You may import read_trips from q2a.
from q2a import read_trips

def get_spending(filename, card, mode=None):
    """
    Return (number of trips, total fare rounded to 2 d.p.) for card.
    """
    results = read_trips(filename)

    total = 0
    count = 0

    for trip in results:
        if card == trip[0] and mode == trip[2]:
            count += 1
            total += trip[3]

        elif card == trip[0] and mode == None:
            count += 1
            total += trip[3]
    total = round(total,2)

    return (count,total)
