# Mock LT2C - Q1 Part A (solution)

def get_good_stalls(stalls, min_rating, min_reviews):
    if stalls == []:                       # empty-case line from the paper, handled first
        return None
    good = []
    for name, rating, reviews in stalls:   # tuple unpacking
        if rating >= min_rating and reviews >= min_reviews:   # both inclusive
            good.append(name)
    return good                            # a NEW list, stalls is untouched
