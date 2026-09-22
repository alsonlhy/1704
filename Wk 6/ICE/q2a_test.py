from q2a import get_unique_titles

print('Testcase 1')
print('-' * 10)
print("Expected: ['Intro to Programming', 'Intro to Python']")
books_list = [("Intro to Programming", "Ed-2", 2, "paperback"), ("Intro to Python", "Ed-1", 5, "paperback"), ("Intro to Programming", "Ed-3", 4, "hardcover")]
print('Actual:   ' + str(get_unique_titles(books_list)))

print('\nTestcase 2')
print('-' * 10)
print("Expected: []")
books_list = []
print('Actual:   ' + str(get_unique_titles(books_list)))