import sys
#import numpy as np

char = ['a','b','c','d','e','f','g','h','i','s']
doors_keys = {'b':'a', 'd':'c', 'g':'f', 'i':'h'}
doors_list = ['b','d','g','i']
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


# Path to be delivered
final_tuple = []


# Step 1
# Read matrix from text file, and save into the grid[]
def read_file(filepath):    
    with open(filepath) as my_txt:        
        # For each line
        for line in my_txt: 
            # Remove line break and spaces
            line = line.split()

            # Add new list to the main grid
            grid.append(line) 
    #print(grid) 
            

    # Run function. Starting from coordiantes of "s"
    #deep_index(grid, "s")               
   # ghost_buster()
   # print(grid)
    print(len(grid[0]) - 1)
    print(len(grid) - 1)


# Step 2
# Search for index of element in sub-list.
# It will return (x,y)
# Replace the 's' with '0'
def deep_index(lst, w):
    for (i, sub) in enumerate(lst):
        if w in sub:            
            loc = sub.index(w)
            sub.remove(w)
            sub.insert(loc, '0')
            search(i, loc)


# Step 3a: Search for ghosts
def ghost_buster():
    for y in range(1,len(grid) - 1):
        for x in range(1,len(grid[0]) - 1):   
            #print(x,y,grid[x][y])  
            gh = grid[x][y]
            if gh == "2" or gh == "3":# or gh == "4":
                mark_sight(x,y,gh)





def mark_sight(x,y,gh):
    range_x = range(0,len(grid[0]) - 1)
    range_y = range(0,len(grid) - 1)

    if y in range_y:
        if x in range_x:
            sight = int(gh) - 1
            
            print(x-sight, y)
            print(x+sight, y)
            print(x, y+sight)
            print(x, y-sight)

            if grid[x-sight][y] == '0' and x-sight in range_x:
                grid[x-sight][y] = 'x'

            if grid[x+sight][y] == '0' and x+sight in range_x:
                grid[x+sight][y] = 'x' 
            
            if grid[x][y-sight] == '0' and y-sight in range_y:
                grid[x][y-sight] = 'x'

            if grid[x][y+sight] == '0' and y+sight in range_y:
                grid[x][y+sight] = 'x'


# Step 3
# Read generated grid and search for path
def search(x, y):
    # e means the end point
    if grid[x][y] == 'e':
        #print('Found at %d,%d' % (x, y))
        final_tuple.append((x, y))
        print(final_tuple)
        return True
    
    # 1 means a wall
    elif grid[x][y] == '1':
        # print('Wall at %d,%d' % (x, y))
        return False
        
    # Found a door
    elif grid[x][y] in doors_list:
        #print('Found Door: ' + grid[x][y])
        
        need_key = doors_keys[grid[x][y]]
        #print('Needed Key: ' + need_key)

        # If we have the key
        if need_key not in keys_list:
            return False
        else:
            keys_list.remove(need_key)
            #print('You can pass')            


    # Found a key
    elif grid[x][y] in doors_keys.values():
        keys_list.append(grid[x][y])
        #print('Found Key: ' + grid[x][y])
        # Remove the visited path
        for l in grid:
            for n, i in enumerate(l):                
                if i == '9':
                    l[n] = '0'


    # 9 means already visited
    elif grid[x][y] == '9' :
        # print('Visited at %d,%d' % (x, y))
        return False


    # Add to tuple
    #print('Visiting %d,%d' % (x, y))    
    final_tuple.append((x, y))
    # print(x, y)

    # Mark as visited
    grid[x][y] = '9'

    # Explore paths clockwise starting from the one on the bottom
    if ((x < len(grid)-1 and search(x+1, y))
        or (y > 0 and search(x, y-1))
        or (x > 0 and search(x-1, y))
        or (y < len(grid)-1 and search(x, y+1))):
        return True
    #print('Visiting previous cell %d,%d' % (x, y))   
    final_tuple.append((x, y))
    return False



#################### STEPS ########################
# Step 1: Read file and generate grid
read_file(filepath)
#deep_index(test_grid, "s")


# Step 2: Search for 's'
# callback of step 2


# Step 3: Run through the grid
# callback of step 3
