filepath = "Maze1.txt"

# Grid containaing the matrix from the text file
grid = []

# To BE delivered
final_tuple = []


# Step 1
# Read matrix from text file, and save into the grid[]
def read_file(filepath):    
    with open(filepath) as my_txt:        
        # For each line
        for line in my_txt: 
            # Remove line break and spaces
            line = line.replace("\n","").split(" ")

            # Add new list to the main grid
            grid.append(line)            
    #print(grid)

    # Run function. Starting from coordiantes of "s"
    deep_index(grid, "s")



# Step 2
# Search for index of element in sub-list.
# It will return (x,y)
def deep_index(lst, w):
    for (i, sub) in enumerate(lst):
        if w in sub:
            print("Starting from: " + str(i) + "," + str(sub.index(w)))
            search(i, sub.index(w))



# Step 3
# Read generated grid and search for path
def search(x, y):
    # Convert numbers from strings to integers
    if grid[x][y] != "e" and grid[x][y] != "s":
        grid[x][y] = int(grid[x][y])

    # e means the end point
    if grid[x][y] == 'e':
        print('found at %d,%d' % (x, y))
        final_tuple.append((x, y))
        print(final_tuple)
        return True
    
    # 1 means a wall
    elif grid[x][y] == 1:
        #print('Wall at %d,%d' % (x, y))
        return False
    
    # 2 means already visited
    elif grid[x][y] == 2:
        #print('Visited at %d,%d' % (x, y))
        return False
    
    # Add to tuple
    #print('Visiting %d,%d' % (x, y))
    final_tuple.append((x, y))
    print(x, y)

    # Mark as visited
    grid[x][y] = 2

    # Explore paths clockwise starting from the one on the right
    if ((x < len(grid)-1 and search(x+1, y))
        or (y > 0 and search(x, y-1))
        or (x > 0 and search(x-1, y))
        or (y < len(grid)-1 and search(x, y+1))):
        return True

    return False



#################### STEPS ########################
# Step 1: Read file and generate grid
read_file(filepath)
#deep_index(test_grid, "s")


# Step 2: Search for 's'
# callback of step 2


# Step 3: Run through the grid
# callback of step 3
