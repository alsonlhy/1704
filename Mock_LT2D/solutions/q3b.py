def to_minutes(hhmm):
    h, m = hhmm.split(':')
    return int(h) * 60 + int(m)

def get_longest_stay(filename):
    inside = {}
    best = None
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if line == '':
                continue
            time, action, plate = line.split(',')
            t = to_minutes(time)
            if action == 'IN':
                inside[plate] = t
            elif plate in inside:
                minutes = t - inside.pop(plate)
                if best is None or minutes > best[1]:   # strictly longer: earliest OUT wins ties
                    best = (plate, minutes)
    return best
