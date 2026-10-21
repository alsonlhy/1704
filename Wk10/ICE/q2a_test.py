from q2a import get_books_cheaper_than

# Test cases used to test your function
print('\nTest case 1:')
print('------------')
print("Expected: " + '\nTurtles All the Way Down\tJohn Green\t$11.99\n' + 
      'Animal Farm and 1984\tGeorge Orwell\t$7.50\n' + 
      'Inception: A Dark Paranormal Romance (The Marked Book 1)\tBianca Scardoni\t$13.09\n')
input_file = 'books-1.txt'
output_file = 'books-1-output.txt'
price_limit = 15.0
get_books_cheaper_than(input_file, price_limit, output_file)
result = 'Open the file books-1-output.txt and verify it contains the expected books listed above.'
print('Actual:   ' + str(result))

print('\nTest case 2:')
print('------------')
print("Expected: Empty file")
input_file = 'books-2.txt'
output_file = 'books-2-output.txt'
price_limit = 7.0
get_books_cheaper_than(input_file, price_limit, output_file)
result = 'Open the file books-2-output.txt and verify it is empty.'
print('Actual:   ' + str(result))

