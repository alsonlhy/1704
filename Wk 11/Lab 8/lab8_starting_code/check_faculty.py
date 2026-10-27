def check_faculty(filename):

    faculty_dict = {}

    with open(filename) as reading: 

        for line in reading:

            line = line.rstrip("\n")
            sch, rm, pax, proj = line.split("\t")

            if sch not in faculty_dict:
                faculty_dict[sch] = [(rm, int(pax), proj)]

            else:
                existing = faculty_dict[sch]
                existing.append((rm, int(pax), proj))

    return faculty_dict