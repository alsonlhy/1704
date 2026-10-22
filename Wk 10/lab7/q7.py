import random

def extract_text(filename):

    extracted = []

    with open(filename) as reading:

        for line in reading:
            line = line.rstrip('\n')
            word = line.split(' ')

            extracted.append(word)

    return extracted

def scramble(word):

    if len(word) <= 3:
        return word

    inner = list(word[1:-1])
    if len(set(inner)) < 2:
        return word

    ori_inner = "".join(inner)
    shuffle_inner = ori_inner

    while shuffle_inner == ori_inner:
        random.shuffle(inner)
        shuffle_inner = "".join(inner)

    return word[0] + shuffle_inner + word[-1]



extracted = extract_text('talk.txt')

new_extract = []

for sentence in extracted:

    new_sentence = []

    for word in sentence:
        new_word = scramble(word)
        new_sentence.append(new_word)

    new_extract.append(new_sentence)

for sentence in new_extract:

    line = ' '.join(sentence)
    print(line + '\n')