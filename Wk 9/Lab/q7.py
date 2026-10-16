def get_lineup(info):

    if info == []:
        return []

    in_front = []
    at_back = []

    for front, behind in info:

        in_front.append(front)
        at_back.append(behind)

    current = ''

    for person in in_front:

        if person not in at_back:
            current = person
            break

    line = []

    while current != "":

        line.append(current)

        for front, behind in info:
            if front == current:
                current = behind
                break

    return line



info = [("Mary", "Jason"), ("John", "Alan"), ("Jason", "George"), ("Alan", "Christie"), ("Christie", "Mary"), ("George", "")]
print(get_lineup(info))