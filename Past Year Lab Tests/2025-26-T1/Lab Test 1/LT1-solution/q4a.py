# Name:
# Email ID:
    
def get_min_allocation(rating):
    # Modify the code below.
    n=len(rating)
    dist=[1]*n
    
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

    return dist