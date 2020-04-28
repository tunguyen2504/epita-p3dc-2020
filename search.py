import sys
#import numpy as np

char = ['a','b','c','d','e','f','g','h','i','s']
keys_doors = {'b':'a', 'c':'d', 'g':'f', 'i':'h'}
doors_list = ['b','c','g','i']
keys_list = []

# Put file path while running
filepath = ""
if len (sys.argv) != 2:
    print('Please put the file name as argument. Ex: python search.py Maze1.txt')
    sys.exit (1)
else:
    filepath = sys.argv[1]



# Grid containaing the matrix from the text file
grid = []

# To Be delivered
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
    if grid[x][y] not in char:
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
        
    # Found a door
    elif grid[x][y] in doors_list:
        print('Found Door: ' + grid[x][y])
        
        need_key = keys_doors[grid[x][y]]
        print('Needed Key: ' + need_key)

        # If we have the key
        if need_key not in keys_list:
            return False
        else:
            keys_list.remove(need_key)
            print('You can pass')
            

    # Found a key
    elif grid[x][y] == 'a':
        keys_list.append(grid[x][y])
        print('Found Key: ' + grid[x][y]) 

        # Remove the visited path
        for l in grid:
            for n, i in enumerate(l):                
                if i == int('9'):
                    l[n] = '0'


    # 9 means already visited
    elif grid[x][y] == 9:
        #print('Visited at %d,%d' % (x, y))
        return False
    

    # Add to tuple
    #print('Visiting %d,%d' % (x, y))
    final_tuple.append((x, y))
    print(x, y)

    # Mark as visited
    grid[x][y] = 9

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
