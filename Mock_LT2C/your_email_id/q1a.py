# Name:
# Email ID:

def get_good_stalls(stalls, min_rating, min_reviews):
    """
    Return the names of stalls rated at least min_rating with at least
    min_reviews reviews, in their original order.
    """
    if stalls == []:

        return None
    new_list = []

    for stall in stalls:
        name = stall[0]
        rating = stall[1]
        num_reviews = stall[2]

        if rating >= min_rating and num_reviews >= min_reviews:
            new_list.append(name)

    
    return new_list
