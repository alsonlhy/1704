# Name:
# Email ID:


def get_swim_report(filename, swimmer_name, event_name):

    count = 0 
    total = 0
    swimmer_data = []
    with open (filename) as reading:

        for line in reading:
            line = line.rstrip("\n")
            columns = line.split(",")

            name = columns[0]
            event = columns[1]
            time = int(columns[2])

            if swimmer_name == name and event_name == event:
                count += 1
                total += time

    if count == 0:
        return (0,0)


    average = round(total/count)
    return (count, average)

        #     swimmer_data.append((name, event, time))

        # for swimmer in swimmer_data:
        #     if swimmer_name == swimmer[0]:

        #         if event_name == swimmer[1]:
        #             count += 1
        #             total += swimmer[2]

    # return (count, average)
        
        

get_swim_report("swimtimes-sample.csv", "Michael Phelps", "50m doggy paddle")