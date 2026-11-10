def convert_time(time_stamp):

    parts = time_stamp.split(":")
    hours = int(parts[0])
    minutes = int(parts[1])
    seconds = int(parts[2][:2])

    if "AM" in parts[2] and hours == 12:
        hours = 0

    elif "PM" in parts[2] and hours != 12:
        hours += 12

    return hours *60 * 60 + minutes * 60 + seconds


def count_emails(file_name, start_time, end_time, sender):

    start_sec = start_time[0] * 3600 + start_time[1] * 60
    end_sec = end_time[0] * 3600 + end_time[1] * 60

    count = 0
    with open (file_name) as reading:

        for line in reading: 
            line = line.rstrip("\n")
            columns = line.split("\t")

            time_stamp = columns[0]
            sending = columns[1]
            receiving = columns[2]


            if sender == sending:

                email_sec = convert_time(time_stamp)
                if start_sec <= email_sec <= end_sec:
                    count += 1
                            


    return count




