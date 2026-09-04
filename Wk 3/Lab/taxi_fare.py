def meter_fare(fare_flag, fare_distance1, fare_distance2, ride_distance):

    if ride_distance < 1000:
        cost = fare_flag

    elif ride_distance <= 9800:
        cost = fare_flag + fare_distance1 * -(-(ride_distance - 1000)//400)

    else:
        cost = fare_flag + fare_distance1 * (8800//400) + fare_distance2 * -(-(ride_distance - 9800)//350)

    return cost

def surcharge(time_surcharge, location):

    total = time_surcharge * meter_fare(fare_flag, fare_distance1, fare_distance2, ride_distance) + location

    return total




fare_flag = float(input("What's the flag-down fare: "))
fare_distance1 = float(input("What's the rate per 400 meters within 9.8km? "))
fare_distance2 = float(input("What's the rate per 350 meters within 9.8km? "))
ride_distance = int(input("What's the distance traveled (in meters)? "))

peak = input("Is the ride during a peak period? [yes/no] ")

if peak == "yes":
    time_surcharge = 0.25


else:
    midnight = input("Is the ride during midnight and 6am? [yes/no] ")

    if midnight == "yes":
        time_surcharge = 0.5

    else:
        time_surcharge = 0


location = input("Is there any location surcharge? [yes/no] ")

if location == "yes":
    location = float(input("What's the amount of location surcharge? "))

else:
    location = 0


final_fare = meter_fare(fare_flag, fare_distance1, fare_distance2, ride_distance) + surcharge(time_surcharge, location)

print(f"The total fare is ${final_fare:.2f}")
