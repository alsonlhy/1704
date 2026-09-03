def meter_fare(fare_flag, fare_distance):

    if ride_distance < 1000:
        cost = fare_flag

    elif ride_distance <= 9800:
        cost = fare_flag + fare_distance * ((ride_distance - 1000)/400)

    else:
        cost = fare_flag + fare_distance * (8800/400) + fare_distance * ((ride_distance - 9800)/350)

    return cost

