# Name:
# Email ID:

def calculate_actual_delays(list_cars, traffic_lights):
    # Replace the code below with your implementation.
    
    # return the delays for all cars, and how many green lights to clear all including the 1st green light
    list_cars_ret = []
    iterations = []

    for lane in list_cars:
        wait_time = 0
        green_duration = traffic_lights[0]
        # all cars for the lane
        list_cars_lane = []
        # start at green light, count as 1
        iteration = 1
        for car in lane:
            if green_duration >= car[1]:
                wait_time += car[1]
                green_duration -= car[1]
                list_cars_lane.append((car[0], wait_time))
            else:
                # add red light and remaining duration of green light to wait_time for next car in the lane
                wait_time += traffic_lights[1] + green_duration + car[1]
                # reset green duration
                green_duration = traffic_lights[0] - car[1]
                # record number of iterations for this lane
                iteration += 1

                list_cars_lane.append((car[0], wait_time))

        # append to the list of cars to be returned
        list_cars_ret.append(list_cars_lane)
        iterations.append(iteration)

    # return a different list with car_id and waiting time
    return list_cars_ret, max(iterations)

