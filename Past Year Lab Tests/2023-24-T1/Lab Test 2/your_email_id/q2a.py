# Name:
# Email ID:

def get_special_word_count(filename):
    # The line of code below is for you to use. DO NOT modify it.
    special_chars = ".,;:!?()[]{}-~&*/+-=%$#@^_'\"<>"

    count = 0 

    with open (filename) as reading:

        for line in reading:
            line = line.rstrip("\n")
            words = line.split(" ")

            for word in words:
                for ch in word:

                    if ch in special_chars:
                        count += 1
    
    return count
