def count_emails(file_name, start_time, end_time, sender):

    # extracted = []
    # with open (file_name) as reading:

    #     for line in reading: 
    #         line = line.rstrip("\n")
    #         columns = line.split("\t")

    #         time_stamp = columns[0]
    #         hms = time_stamp.split(":")
    #         hh = hms[0]
    #         mm = hms[1]
    #         ss = hms[2]

    #         sending = columns[1]
    #         receiving = columns[2]

    #         extracted.append([hh, mm, ss, sending, receiving])

    # count = 0
    # for lst in extracted:

    #     hour = int(lst[0])
    #     minute = int(lst[1])
    #     sec = int(lst[2][:2])
    #     send = lst[3]
    #     receive = lst[4]

    #     if "PM" in lst[2] and (hour < 12 and hour != 12):
    #         hour += 12

    #     if sender == send and (hour >= start_time[0] and hour <= end_time[0]):
            
    #         if (minute >= start_time[1] or minute <= end_time[1]):

    #             if sec == 0:
    #                 count += 1
    #                 # print(lst)
                            


    # return count

# print(count_emails('emails-1.txt',0,0,0))
    
    pass



