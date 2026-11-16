# Name:
# Email ID:

def get_unreturned(filename):
    not_returned = []
    with open(filename) as reading:
        reading.readline()
        for line in reading:
            line = line.rstrip("\n")
            member, book, borrowed, returned = line.split(",")

            if returned == "-":
                not_returned.append((member,book))

        return not_returned
