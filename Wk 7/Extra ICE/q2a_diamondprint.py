def print_diamond(n):
    for r in range(2 * n - 1):          # row number 0 .. 2n-2
        if r < n:
            i = r                       # top half: distance grows
        else:
            i = 2 * n - 2 - r           # bottom half: mirror image

        line = " " * (n - 1 - i) + "*"  # indent, then first star
        if i > 0:
            line += " " * (2 * i - 1) + "*"   # gap, then second star
        print(line)



print_diamond(6)