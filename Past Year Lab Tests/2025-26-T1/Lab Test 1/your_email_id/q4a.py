# Name:
# Email ID:
    
def get_min_allocation(rating):

    n = len(rating)
    points = [1] * n

    for i in range(1,n):
        if rating[i] > rating[i-1]:
            points[i] = points[i-1] + 1

    for i in range(n-2,-1,-1):
        if rating[i] > rating[i+1]:
            points[i] = max(points[i], points[i+1]+1)
    
    return points
