def get_member_summary(filename):
    summary = {}
    with open(filename) as f:
        f.readline()
        for line in f:
            line = line.strip()
            if line == '':
                continue
            member, book, borrowed, returned = line.split(',')
            loans, out = summary.get(member, (0, 0))
            loans += 1
            if returned == '-':
                out += 1
            summary[member] = (loans, out)
    return summary
