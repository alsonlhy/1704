def print_diamond_using_str(text):
    L = len(text)
    n = L // 4 + 1                          # side length

    for r in range(2 * n - 1):              # 2n - 1 rows
        i = r if r < n else 2 * n - 2 - r   # distance from the nearest tip

        line = " " * (n - 1 - i) + text[r]  # indent, then left character
        if i > 0:                           # not a tip: add gap and right character
            line += " " * (2 * i - 1) + text[L - r]
        print(line)


print_diamond_using_str('12345678')