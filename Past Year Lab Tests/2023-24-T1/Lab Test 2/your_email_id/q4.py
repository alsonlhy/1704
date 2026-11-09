# Name:
# Email ID:

def calculate_actual_delays(list_cars, traffic_lights):

    green = traffic_lights[0]
    red = traffic_lights[1]

    all_lanes = []
    count = 1

    for lane in list_cars:
        time = 0
        lane_result = []
        remaining = green
        cycle = 1

        for car in lane:
            car_id = car[0]
            delay = car[1]

            if delay > remaining: 
                time += remaining + red
                cycle += 1
                remaining = green

            time += delay
            remaining -= delay
            lane_result.append((car_id, time))

        all_lanes.append(lane_result)

        if cycle > count:
            count = cycle
    

    return_tup = (all_lanes, count)


    
    return return_tup