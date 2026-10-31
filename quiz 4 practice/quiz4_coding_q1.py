with open('tours.txt', 'w') as writing:

    writing.write('TOUR!PLACES!PRICE' + '\n')
    writing.write('River Walk!12!18.50' + '\n')
    writing.write('Heritage Trail!8!24.00' + '\n')
    writing.write('Garden Visit!15!16.00' + '\n')
    writing.write('Night Tour!6!28.50' + '\n')    


def read_tours(filename):

    newlist = []

    with open(filename) as reading:

        for line in reading:

            line = line.rstrip('\n')
            tour_name, avail_place, ppp = line.split("!")

            tup = (tour_name, avail_place, ppp)
            newlist.append(tup)


    return tup

print(read_tours("tours.txt"))