def to_minutes(hhmm):
    h, m = hhmm.split(':')
    return int(h) * 60 + int(m)

def all_subsets(items):
    subsets = [[]]
    for x in items:
        new = []
        for s in subsets:
            new.append(s + [x])
        subsets = subsets + new
    return subsets

def no_clashes(group):
    for i in range(len(group)):
        for j in range(i + 1, len(group)):
            a, b = group[i], group[j]
            if a[1] < b[2] and b[1] < a[2]:
                return False
    return True

def get_best_workshops(filename):
    workshops = []
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if line == '':
                continue
            wid, start, end, points = line.split(',')
            workshops.append((wid, to_minutes(start), to_minutes(end), int(points)))

    best_total, best_ids = 0, []
    for combo in all_subsets(workshops):
        if not no_clashes(combo):
            continue
        total = 0
        for w in combo:
            total += w[3]
        ids = sorted([w[0] for w in combo])
        if (total > best_total
                or (total == best_total and len(ids) < len(best_ids))
                or (total == best_total and len(ids) == len(best_ids) and ids < best_ids)):
            best_total, best_ids = total, ids
    return (best_total, best_ids)
