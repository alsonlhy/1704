# Name:
# Email ID:

def decode_potter(filename):
    """
    Extract strings from a file of encoded text

    Args:
        filename (str): The name of the file to read.

    Returns:
        list: A list of strings extracted from each line of the file
    """
    extracted = []

    with open (filename) as reading: 

        for line in reading: 
            line = line.rstrip("\n")
            sen_length = int(line[0:3])


            if sen_length == 0:
                sentence = ""

            else:
                sentence = line[3:(sen_length+3)]

            extracted.append(sentence)


    
    return extracted
