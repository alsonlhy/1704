# =====
# q1.py
# =====
# Name: 
# Email ID:

def get_hashtags(post_list):

    hashed_words = []

    for string in post_list:


        split_word = string.split(" ")

        for element in split_word:
            if "#" in element:
                hashed_words.append(element)

    return hashed_words
