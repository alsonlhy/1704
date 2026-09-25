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
    # Modify the code below.
    list_to_return = []
    with open(filename, 'r') as my_file:
        for line in my_file:
            line = line.rstrip('\n')
            text_length = int(line[0:3])
            text = line[3: 3+text_length]
            list_to_return.append(text)

    return list_to_return
