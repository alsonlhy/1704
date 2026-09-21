# Name:
# Email ID:

# Solution 1: scan the string character by character and collect the numbers
# Key idea: we are told digits and '.' appear ONLY inside a height, so every
# run of digits/'.' in the string is exactly one height.

def compute_avg_height(heights_str):
    total = 0.0
    count = 0
    number_str = ''      # the number we are currently building up

    for ch in heights_str:
        if ch.isdigit() or ch == '.':
            # still inside a number -> keep collecting
            number_str += ch
        else:
            # we just left a number -> the number is complete
            if number_str != '':
                total = total + float(number_str)
                count = count + 1
                number_str = ''      # reset, ready for the next height

    # don't forget a number that ends at the very end of the string!
    if number_str != '':
        total = total + float(number_str)
        count = count + 1

    if count == 0:    # For this question, not needed because "•	The string parameter contains at least one person’s height"
        return 0.0

    return total / count

# Solution 2: split on ':' first, then read the number at the start of each piece
def compute_avg_height(heights_str):
    # a name never contains ':', so every ':' separates a name from a height
    parts_list = heights_str.split(':')

    total = 0.0
    count = 0

    # part 0 is only a name, so start from index 1
    for i in range(1, len(parts_list)):
        part = parts_list[i]
        
        number_str = ''
        for ch in part:
            if ch.isdigit() or ch == '.':
                number_str += ch
            elif number_str != '':
                # we already have the number and just hit 'm' (or a space
                # after it) -> stop, the rest of this part is the next name
                break

        if number_str != '':
            total = total + float(number_str)
            count = count + 1

    if count == 0:
        return 0.0

    return total / count
