def compress(s):
    result = ''
    i = 0
    while i < len(s):
        j = i
        while j < len(s) and s[j] == s[i]:   # walk to the end of this run
            j += 1
        run = j - i
        result += s[i]
        if run > 1:
            result += str(run)
        i = j
    return result
