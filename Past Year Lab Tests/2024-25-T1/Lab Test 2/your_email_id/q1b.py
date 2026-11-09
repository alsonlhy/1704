# Name:
# Email ID:

def alternate_and_reverse(s1, s2):
    result = ""
    shorter = min(len(s1), len(s2))

    # alternate characters for the length of the shorter string
    for i in range(shorter):
        result += s1[i] + s2[i]

    # pick whichever string has leftover characters
    if len(s1) > len(s2):
        longer = s1
    else:
        longer = s2

    # append the leftover characters in reverse order
    for i in range(len(longer) - 1, shorter - 1, -1):
        result += longer[i]

    return result