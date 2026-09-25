# Name:
# Email ID:

def get_special_word_count(filename):
    # The line of code below is for you to use. DO NOT modify it.
    special_chars = ".,;:!?()[]{}-~&*/+-=%$#@^_'\"<>"
    
    # Replace the code below with your implementation.
    cnt = 0
    with open(filename, 'r') as input_file:
        for line in input_file:
            line = line.rstrip('\n')
            words = line.split(' ')
            for word in words:
                for ch in word:
                    if ch in special_chars:
                        cnt += 1
    return cnt
	
