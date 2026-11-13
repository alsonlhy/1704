# Name:
# Email ID:
from q2a import decode_potter


def decode_potter_checksum(filename):
    """
    Extract strings from a file of encoded text and compare
    the computed checksum against the expected checksum to 
    detect data corruption.

    Args:
        filename (str): The name of the file to read.

    Returns:
        list[tuple(str, int, bool)]: A list of tuples,
          with one tuple for each line of the file.  
        * str: the text extracted from the message
        * int: the calculated checksum for this message
        * bool: True if calculated checksum is equal to expected checksum
    """ 
    sentences = decode_potter(filename)
    check = []
    vowel_check = "AaEeIiOoUu"


    for sentence in sentences:

        text = sentence[:-2]
        checksum = int(sentence[-2:])
        count = 0
        for letter in text:
            if letter in vowel_check:
                count += 1

        if count == checksum:
            check.append((text, count, True))
        else:
            check.append((text,count,False))

    return check
