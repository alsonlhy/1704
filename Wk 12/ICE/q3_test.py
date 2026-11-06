
# ### Q3: HTML
# SOLUTION

from q3 import extract_bold_texts
# Test cases used to test your function

print('\nTestcase 1')
print('-' * 10)
html_text = '<b>ABC</b> abc <b>def 123 </b><b></b>0000'
print("Expected: ['ABC', 'def 123 ', '']")
print('Actual:   ' + str(extract_bold_texts(html_text)))

print('\nTestcase 2')
print('-' * 10)
html_text = 'A piece of text without tags.'
print("Expected: []")
print('Actual:   ' + str(extract_bold_texts(html_text)))

