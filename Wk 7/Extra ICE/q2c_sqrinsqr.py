def print_squares(n):
    for r in range(n):                      # each row
        line = ""
        for c in range(n):                  # each column
            ring = min(r, c, n - 1 - r, n - 1 - c)
            if ring % 2 == 0:
                line += "*"
            else:
                line += " "
        print(line)


print_squares(7)