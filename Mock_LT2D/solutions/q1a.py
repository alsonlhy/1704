def get_longest_streak(steps, goal):
    if steps == []:
        return None
    best = 0
    current = 0
    for n in steps:
        if n >= goal:
            current += 1
            if current > best:
                best = current
        else:
            current = 0
    return best
