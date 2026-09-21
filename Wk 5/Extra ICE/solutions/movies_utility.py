# Name:
# Email ID:

# Each movie is a tuple: (title, genre, duration_in_minutes)
# The four functions below belong in a SEPARATE file called movies_utility.py.
# The given file movies.py then does:
#
#     import movies_utility
#     ...
#     print(movies_utility.get_average_duration(movie_list))
#
# Each movie is a tuple: (title, genre, duration_in_minutes)
#   movie[0] -> title      movie[1] -> genre      movie[2] -> duration

# Solution
def get_average_duration(movie_list):
    # handle empty list first (avoid division by zero)
    if len(movie_list) == 0:
        return 0.0

    total_duration = 0
    for movie in movie_list:
        total_duration = total_duration + movie[2]

    return total_duration / len(movie_list)


def get_num_movies_of_genre(movie_list, genre):
    # a counter grown outside of the for loop
    count = 0
    for movie in movie_list:
        if movie[1] == genre:
            count = count + 1

    # an empty list simply never enters the loop, so 0 is returned
    return count


def get_title_of_longest_movie(movie_list):
    # handle empty list first
    if len(movie_list) == 0:
        return ''

    # same "champion" pattern as get_longest_str() in the main exercises
    longest_movie = movie_list[0]
    for movie in movie_list:
        if movie[2] > longest_movie[2]:
            longest_movie = movie

    return longest_movie[0]


def get_movies_with_keyword(movie_list, keyword):
    # grow a NEW list outside of the for loop
    list_to_return = []
    for movie in movie_list:
        # 'in' tests whether keyword is a substring of the title
        if keyword in movie[0]:
            list_to_return.append(movie)

    # an empty list simply never enters the loop, so [] is returned
    return list_to_return
