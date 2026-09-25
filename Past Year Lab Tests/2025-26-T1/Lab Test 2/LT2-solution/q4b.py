# Name:
# Email ID:

def help_frog_against_snakes_2(map_lines):
    # Modify the code below.
    # Step 1: Read the 2D map
    lines = map_lines
    
    m = len(lines)        # number of rows
    n = len(lines[0])     # number of columns

    # Step 2: Initialize DP table: each cell stores list of sequences
    dp = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append([])
        dp.append(row)
    #dp = [[[] for _ in range(n)] for _ in range(m)]
    
    dp[0][0] = [[]]       # starting at A

    # Step 3: Iterate through all cells
    for i in range(m):
        for j in range(n):
            if len(dp[i][j])!=0:  # if no way to reach this cell, do nothing
                for seq in dp[i][j]:
                    # Rightward jumps
                    for step in [1, 2, 3]:
                        nj = j + step
                        if nj < n and lines[i][nj] != '*':
                            dp[i][nj].append(seq + [(step, 'r')])
                    # Downward jumps
                    for step in [1, 2, 3]:
                        ni = i + step
                        if ni < m and lines[ni][j] != '*':
                            dp[ni][j].append(seq + [(step, 'd')])

    # Step 4: Extract results from cell B
    total = len(dp[m-1][n-1])
    
    if total == 0:
        return (0, [])
    else:
        return (total, dp[m-1][n-1])

