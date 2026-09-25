# Name:
# Email ID:


def get_swim_report(filename, swimmer_name, event_name):
    # Replace the code below with your implementation.
    tot_time = 0
    num_events = 0
    with open(filename, 'r') as my_file:
        for line in my_file:
            swimmer, event, time_str = line .split(',')
            if swimmer == swimmer_name and event == event_name:
                tot_time += int(time_str)
                num_events += 1
    if tot_time == 0:
        return (0, 0)

    avg = round(tot_time / num_events)
    return (num_events, avg)
        
        

