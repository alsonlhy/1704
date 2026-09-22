# Name:
# Email ID:

def get_unique_titles(books_list):

    unique = []

    for tup in books_list:
        if tup[0] not in books_list:
            unique.append(tup[0])

    return unique