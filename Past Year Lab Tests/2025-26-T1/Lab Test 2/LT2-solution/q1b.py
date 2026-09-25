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
    # Modify the code below.
    sentence_cleaned = clean_sentence(sentence)
    return sentence_cleaned.split(' ')