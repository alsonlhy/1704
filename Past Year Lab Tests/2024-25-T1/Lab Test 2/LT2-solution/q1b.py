# Name:
# Email ID:

def alternate_and_reverse(s1, s2):
    # Replace the code below with your implementation.
    min_length = min(len(s1), len(s2))

    result_str = ""
    for i in range(min_length):
        result_str += s1[i]
        result_str += s2[i]

    result_str += s1[min_length:][::-1]
    result_str += s2[min_length:][::-1]

    return result_str


