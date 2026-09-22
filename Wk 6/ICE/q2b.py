# Name:
# Email ID:
import q2a

def get_titles_and_counts(books_list):

    if len(books_list) == 0:
        return []

    unique_titles_list = q2a.get_unique_titles(books_list)
    new_list = []

    for title in unique_titles_list:

        count = 0

        for tup in books_list:
            current_title = tup[0]
            if current_title == title:
                current_num_copies = tup[2]
                count += current_num_copies

        new_list.append((title,count))

    return new_list