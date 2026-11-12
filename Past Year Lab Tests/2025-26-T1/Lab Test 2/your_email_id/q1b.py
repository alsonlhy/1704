# Name:
# Email ID:


# This function is given to you
# -----------------------------
def clean_sentence(sentence):
    for ch in "!?,.:;":
        sentence = sentence.replace(ch, " ")
    return sentence
# ------------------------------

def extract_words(sentence):

    new_list = []

    word = clean_sentence(sentence).split(" ")


    return word