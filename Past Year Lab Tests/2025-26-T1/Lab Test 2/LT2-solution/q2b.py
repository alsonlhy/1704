# Name:
# Email ID:

from q2a import decode_potter

def get_num_vowels(sentence):
    num_vowels = 0
    for ch in sentence:
        if ch in 'AaEeIiOoUu':
            num_vowels += 1
    return num_vowels

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
    # Modify the code below.

    list_to_return = []
    sentences = decode_potter(filename)
    
    for sentence in sentences:
        text = sentence[0:len(sentence)-2]
        checksum = int(sentence[len(sentence)-2:len(sentence)])
        num_vowels = get_num_vowels(text)
        is_valid_sentence = True
        if num_vowels != checksum:
            is_valid_sentence = False
        list_to_return.append( (text, num_vowels, is_valid_sentence) )
    return list_to_return