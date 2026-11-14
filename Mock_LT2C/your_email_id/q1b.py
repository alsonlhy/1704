# Name:
# Email ID:

def get_initials(names):
    """
    Return the initials of each name in upper case, joined by "-".
    """

    if names == '':
        return ''

    initials = []

    people = names.split(";")
    for person in people:

        words = person.split()
        if not words:
            continue

        person_initial = ''
        for word in words:
            person_initial += word[0].upper()

        initials.append(person_initial)



    return '-'.join(initials)
