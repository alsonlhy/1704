def encode_message(text):

    if text == "":

        return ""
    

    new_text = ""
    current = text[0]
    count = 1

    for ch in text[1:]:

        if ch == current:
            count += 1

        else:
            new_text += current + str(count) + " "
            current = ch
            count = 1

    new_text += current + str(count)
    return new_text


print(encode_message('aaabbcccccde'))

print(encode_message('112333&&$9999999999'))