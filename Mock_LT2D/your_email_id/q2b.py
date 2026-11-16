# Name:
# Email ID:

def get_member_summary(filename):
    summary_dict = {}
    with open(filename) as reading:
        reading.readline()

        for line in reading:
            line = line.rstrip("\n")
            member, book, borrowed, returned = line.split(",")

            if member not in summary_dict:


                summary_dict[member] = (0,0)

            b_count, ur_count = summary_dict[member]
            b_count += 1
            if returned == "-":
                ur_count += 1
            summary_dict[member] = (b_count, ur_count)
            
    return summary_dict
