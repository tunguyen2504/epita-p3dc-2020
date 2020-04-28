grid = [ 
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 1, 1],
    [1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 0, 1, 2, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

def search(x, y):
    # Reached the end
    if grid[x][y] == 2:
        print('found at %d,%d' % (x, y))
        return True
    # Reached a wall
    elif grid[x][y] == 1:
        print('wall at %d,%d' % (x, y))
        return False
    # Already visited
    elif grid[x][y] == 3:
        print('visited at %d,%d' % (x, y))
        return False
    
    # Visiting square
    print('visiting %d,%d' % (x, y))

    # Mark as visited
    grid[x][y] = 3

    # Explore neighbors clockwise starting by the one on the right
    if ((x < len(grid)-1 and search(x+1, y))
        or (y > 0 and search(x, y-1))
        or (x > 0 and search(x-1, y))
        or (y < len(grid)-1 and search(x, y+1))):
        return True

    return False

# Run function. Starting from 1,1
search(1, 1)