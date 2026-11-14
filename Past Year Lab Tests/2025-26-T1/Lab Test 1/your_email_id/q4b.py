# Name:
# Email ID:
    
def get_min_allocation_grid(rating_grid):

    rows = len(rating_grid)
    cols = len(rating_grid[0])

    # Rule 1: Everyone starts with 1 bonus point
    points = [[1] * cols for _ in range(rows)]

    # Directions for up, down, left, right neighbors
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    changed = True
    while changed:
        changed = False

        for r in range(rows):
            for c in range(cols):
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    # Check if neighbor is inside grid boundaries
                    if 0 <= nr < rows and 0 <= nc < cols:
                        # Rule 2: Higher rating than neighbor -> strictly more points
                        if rating_grid[r][c] > rating_grid[nr][nc]:
                            if points[r][c] <= points[nr][nc]:
                                points[r][c] = points[nr][nc] + 1
                                changed = True

    
    return points
