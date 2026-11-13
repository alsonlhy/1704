# Mock LT2C - Q1 Part B (solution)

def get_initials(names):
    groups = []
    for name in names.split(';'):
        words = name.split()               # split() with no argument copes with extra spaces
        if words == []:                    # skip empty segments such as ';;' or ';  ;'
            continue
        initials = ''
        for word in words:
            initials += word[0].upper()
        groups.append(initials)
    return '-'.join(groups)                # '' when there are no names
