# Name:
# Email ID:
    
def help_frog_against_snakes(map):
    # Modify the code below.

    
    # Extract map between 'A' and 'B'
    map_str = map[1 : -1]
    n = len(map_str)
    
    # Step 2: DP table: dp[i] = list of jump sequences to reach position i
    # position 0 means after A (before first cell)
    dp = []
    for i in range(n+2):
        dp.append([])
    dp[0] = [[]]  # one way to start (no jumps yet)
    

    # Step 3: Fill DP table iteratively
    for i in range(n + 2):  # include B as position n+1
        for seq in dp[i]:
            for jump in [1, 2, 3]:
                next_pos = i + jump
                if next_pos <= n+1:
                    # If landing at B, or it's safe
                    if next_pos == n+1 or map_str[next_pos - 1] != '*':
                    # Append new sequence
                        dp[next_pos].append(seq + [jump])
    
    # Step 4: Return total and all sequences reaching B
    total = len(dp[n+1])
    return (total, dp[n+1])

