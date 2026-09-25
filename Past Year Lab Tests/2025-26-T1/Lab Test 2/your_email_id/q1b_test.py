from q1b import extract_words

print("\nTest Case 1: extract_words(sentence)")
print("------------------------------------")
sentence = "Hello!world?Python,rocks"
print('sentence = "' + sentence + '"')
result = extract_words(sentence)
print()
print("Expected: ['Hello', 'world', 'Python', 'rocks']")
print('Actual:   ' + str(result))

print("\nExpected type of returned value: <class 'list'>")
print('Actual type of returned value:   ' + str(type(result)))
print()


print("\nTest Case 2: extract_words(sentence)")
print("------------------------------------")
sentence = "apple;banana:cherry"
print('sentence = "' + sentence + '"')
result = extract_words(sentence)
print()
print("Expected: ['apple', 'banana', 'cherry']")
print('Actual:   ' + str(result))
print()


print("\nTest Case 3: extract_words(sentence)")
print("------------------------------------")
sentence = "Go.Go!Go"
print('sentence = "' + sentence + '"')
result = extract_words(sentence)
print()
print("Expected: ['Go', 'Go', 'Go']")
print('Actual:   ' + str(result))
print()



