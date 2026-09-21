# Name:
# Email ID:

def reverse_words(text):
   # split the text into a list of words, using ' ' as delimiter
      word_list = text.split(' ')
  
      # grow a string outside of the for loop
      s_to_return = ''
      for word in word_list:
          # word[::-1] walks the string backwards -> a reversed copy
          s_to_return += word[::-1] + ' '
  
      # there is always one extra ' ' at the end that needs to be removed
      # (for an empty text, s_to_return is just ' ', so this returns '')
      return s_to_return[0:len(s_to_return) - 1]
  
