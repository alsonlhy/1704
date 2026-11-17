# Name: Alson Lam   
# Email ID: alson.lam.2026

def bike_usage(filename):
    """
    Return a dict mapping bike_id -> [number_of_trips, total_duration_min]

    Args:
        filename (str): The name of the trip file to read
    
    Returns:
        dict mapping bike_id (str) -> list[int] of the form
        [number_of_trips, total_duration_min] for that bike.
        An empty dict is returned if the file contains no trips.
    """

    bike_dict = {}
    
    with open (filename) as reading:

        reading.readline()

        for line in reading:
            line = line.rstrip("\n")
            columns = line.split(",")
            if line == '':
                continue

            trip_id = columns[0]
            bike_id = columns[1]
            from_stn = columns[2]
            to_stn = columns[3]
            depart_time = columns[4]
            duration_min = int(columns[5])

            if bike_id not in bike_dict:
                bike_dict[bike_id] = [1, duration_min]

            else:
                bike_count, total_duration = bike_dict[bike_id]
                bike_count += 1
                total_duration += duration_min
                bike_dict[bike_id] = [bike_count, total_duration]
    return bike_dict
