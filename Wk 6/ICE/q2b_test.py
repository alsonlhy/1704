from q2b import get_titles_and_counts

print('Testcase 1')
print('-' * 10)
print("Expected: [('Intro to Programming', 6), ('Intro to Python', 8)]")
books_list = ([("Intro to Programming", "Ed-2", "paperback", 2), ("Intro to Python", "Ed-1", "paperback", 5), ("Intro to Programming", "Ed-3", "hardcover", 4), ("Intro to Python", "Ed-3", "hardcover", 3)])
print('Actual:   ' + str(get_titles_and_counts(books_list)))

print('\nTestcase 2')
print('-' * 10)
print("Expected: []")
books_list = []
print('Actual:   ' + str(get_titles_and_counts(books_list)))