# Name:
# Email ID:

def get_longest_streak(steps, goal):

    if steps == []:
        return None

    current = 0
    best = 0
    for step in steps:
        if step >= goal:
            current += 1

            if current > best:
                best = current

        else:
            current = 0

    
    return best
