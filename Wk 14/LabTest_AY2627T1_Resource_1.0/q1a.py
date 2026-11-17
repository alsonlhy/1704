# Name: Alson Lam   
# Email ID: alson.lam.2026

def count_problematic_trips(trips):
    """
    Return the number of problematic bus trips.

    Args:
        trips (list[tuple]): A list or tuples representnig bus trips. Each tuple 
        contains 3 elements: (route_number, number_of_passengers, delay_minutes)
    Returns:
        int: The number of problematic bus trips.
    """

    if trips == []:
        return 0

    count = 0

    for tup in trips:
        route_num = tup[0]
        num_passenger = tup[1]
        delay = tup[2]

        if num_passenger > 40 or delay >= 10:
            count += 1

    return count

