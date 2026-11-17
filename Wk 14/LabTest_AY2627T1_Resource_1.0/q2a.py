# Name: Alson Lam
# Email ID: alson.lam.2026

def classify_messages(messages):
    """
    Classifies a list of messages according to rules specified in the test paper.

    Args:
        messages (list[str]): a list of messages of type string.
    
    Returns:
        list[tuple]: A list of tuples. 
        Each tuple contains the message associated to a category:
        - 'E' : empty message
        - 'U' : urgent message
        - 'Q' : question
        - 'L' : long message
        - 'N' : normal message
    """
    
    new_list = []

    for message in messages:
        if message == "":
            new_list.append((message, 'E'))

        elif message.split(":")[0] == 'URGENT':
            new_list.append((message, 'U'))

        elif message[-1] == "?":
            new_list.append((message, 'Q'))

        elif len(message) > 25:
            new_list.append((message, 'L'))

        else:
            new_list.append((message, 'N'))      
    
    return new_list
