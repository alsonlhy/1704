# Name:
# Email ID:
    
def row_adjust(rating, dist):
    n=len(rating)
    for i in range(n-1):
        if rating[i]>rating[i+1] and dist[i]<=dist[i+1]:
            dist[i]=dist[i+1]+1
        elif rating[i]<rating[i+1] and dist[i]>=dist[i+1]:
            dist[i+1]=dist[i]+1
    for i in range(n-1,0,-1):
        if rating[i]>rating[i-1] and dist[i]<=dist[i-1]:
            dist[i]=dist[i-1]+1
        elif rating[i]<rating[i-1] and dist[i]>=dist[i-1]:
            dist[i-1]=dist[i]+1

def get_min_allocation_grid(rating_grid):
    m=len(rating_grid)
    n=len(rating_grid[0])
    
    dist_grid=[1]*m
    for r in range(m):
        dist_grid[r]=[1]*n

    for r in range(m): 
        row_adjust(rating_grid[r], dist_grid[r])

    for c in range(n):
        for i in range(m-1):
            if rating_grid[i][c]>rating_grid[i+1][c] and dist_grid[i][c]<=dist_grid[i+1][c]:
                dist_grid[i][c]=dist_grid[i+1][c]+1
                row_adjust(rating_grid[i], dist_grid[i])
            elif rating_grid[i][c]<rating_grid[i+1][c] and dist_grid[i][c]>=dist_grid[i+1][c]:
                dist_grid[i+1][c]=dist_grid[i][c]+1
                row_adjust(rating_grid[i+1], dist_grid[i+1])
        for i in range(m-1,0,-1):
            if rating_grid[i][c]>rating_grid[i-1][c] and dist_grid[i][c]<=dist_grid[i-1][c]:
                dist_grid[i][c]=dist_grid[i-1][c]+1
                row_adjust(rating_grid[i], dist_grid[i])
            elif rating_grid[i][c]<rating_grid[i-1][c] and dist_grid[i][c]>=dist_grid[i-1][c]:
                dist_grid[i-1][c]=dist_grid[i][c]+1
                row_adjust(rating_grid[i-1], dist_grid[i-1])

    for c in range(n-1,-1,-1):
        for i in range(m-1):
            if rating_grid[i][c]>rating_grid[i+1][c] and dist_grid[i][c]<=dist_grid[i+1][c]:
                dist_grid[i][c]=dist_grid[i+1][c]+1
                row_adjust(rating_grid[i], dist_grid[i])
            elif rating_grid[i][c]<rating_grid[i+1][c] and dist_grid[i][c]>=dist_grid[i+1][c]:
                dist_grid[i+1][c]=dist_grid[i][c]+1
                row_adjust(rating_grid[i+1], dist_grid[i+1])
        for i in range(m-1,0,-1):
            if rating_grid[i][c]>rating_grid[i-1][c] and dist_grid[i][c]<=dist_grid[i-1][c]:
                dist_grid[i][c]=dist_grid[i-1][c]+1
                row_adjust(rating_grid[i], dist_grid[i])
            elif rating_grid[i][c]<rating_grid[i-1][c] and dist_grid[i][c]>=dist_grid[i-1][c]:
                dist_grid[i-1][c]=dist_grid[i][c]+1
                row_adjust(rating_grid[i-1], dist_grid[i-1])

    return dist_grid
