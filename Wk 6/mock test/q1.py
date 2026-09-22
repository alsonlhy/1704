# =====
# q1.py
# =====
# Name: 
# Email ID:

def get_hashtags(post_list):

    hashed_words = []

    for i in range(len(post_list)):

        word = post_list[i]

        split_word = word.split(" ")

        for element in split_word:
            if "#" in element:
                hashed_words.append(element)

    return hashed_words
