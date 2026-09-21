def reverse_words(txt):

    new_txt = ""
    split = txt.split(' ')

    for word in split:
        flipped = word[::-1]

        new_txt += flipped + " "

    return new_txt[0:len(new_txt) - 1]


print(reverse_words("Hi there"))