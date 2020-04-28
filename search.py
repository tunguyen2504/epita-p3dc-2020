filepath = "Maze3.txt"
grid = []


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

    # Run function. Starting from 1,1
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
    if grid[x][y] == "1" or grid[x][y] == "3" or grid[x][y] == "0":
        grid[x][y] = int(grid[x][y], base=10)


    if grid[x][y] == 'e':
        print('found at %d,%d' % (y, x))
        return True
    elif grid[x][y] == 1:
        print('wall at %d,%d' % (y, x))
        return False
    elif grid[x][y] == 3:
        #print('visited at %d,%d' % (y, x))
        return False
    
    print('visiting %d,%d' % (y, x))

    # mark as visited
    grid[x][y] = 3

    # explore neighbors clockwise starting by the one on the right
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
