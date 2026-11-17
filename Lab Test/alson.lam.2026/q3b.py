# Name: Alson Lam
# Email ID: alson.lam.2026

def hhmm_to_minutes(text):
    """'09:30' -> 570"""
    h, m = text.split(':')
    return int(h) * 60 + int(m)

def minutes_to_hhmm(minutes):
    """570 -> '09:30'"""
    return f"{minutes // 60:02d}:{minutes % 60:02d}"


def station_balance(filename, window_start, window_end):
    """
    Return a dict mapping station -> (departures, arrivals, net)

    Args:
        filename (str): The name of the trip file to read
        window_start (str): Start of the window, 'HH:MM' (inclusive)
        window_end (str): End of the window, 'HH:MM' (inclusive)
    
    Returns:
        dict mapping station (str) -> tuple(int, int, int), where the tuple is
        (departures, arrivals, net) with net = arrivals - departures.
        Only stations with at least one departure or arrival in the window
        are included. An empty dict is returned if there are none.
    """

    new_dict = {}
    trip_list = []
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
            depart_time = hhmm_to_minutes(columns[4])
            duration_min = int(columns[5])
            arr_time = depart_time + duration_min

            start_min = hhmm_to_minutes(window_start)
            end_min = hhmm_to_minutes(window_end)

            trip_list.append((from_stn, to_stn, depart_time, arr_time))
            dep = 0
            arr = 0
            nett = arr - dep
            # if depart_time >= start_min:
            #     if from_stn not in new_dict:
            #         dep += 1
            #         new_dict[from_stn] = (dep, arr, nett)

            #     else:
            #         departure, arrival, net = new_dict[from_stn]
            #         if arr_time <= end_min:
            #             arrival += 1
            #             net = arrival - departure
            #         new_dict[from_stn] = (departure, arrival, net)
    return new_dict
