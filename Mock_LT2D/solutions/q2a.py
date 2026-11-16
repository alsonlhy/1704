def get_unreturned(filename):
    result = []
    with open(filename) as f:
        f.readline()                          # skip header
        for line in f:
            line = line.strip()
            if line == '':
                continue
            member, book, borrowed, returned = line.split(',')
            if returned == '-':
                result.append((member, book))
    return result
