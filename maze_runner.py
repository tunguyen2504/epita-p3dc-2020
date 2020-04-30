
# coding: utf-8

# In[1]:


# Class to read a maze from a file
class Reader:
    def __init__(self):
        self.grid = []
    
    def read_file(self, file_path):
        with open(file_path) as my_txt:        
            # For each line
            for line in my_txt: 
                # Remove line break and spaces
                line = line.replace("\n","").split(" ")
                # Add new list to the main grid
                self.grid.append(line)            
        print("Maze\n")
        for line in self.grid:
            print(line)


# In[8]:


class Runner:
    def __init__(self, grid):
        self.grid = grid
        self.new_grid = []
        self.start = {}
        self.path = []
        self.key_dict = {"f":"g", "c":"d", "a":"b", "h":"i"}
        self.key_location = {}
        self.door_location = {}
        self.has_key = False
        
#     # to locate the start position
#     def locate_start_end(self, pos, i, j):
#         if (pos == 's'):
#             self.start = (i,j)
#         elif (pos == 'e'):
#             self.start = (i,j)
        
    # to find if the step is blocked
    def is_dead_end(self, x, y, maze):
        neighbor_wall_count = 0
        if (maze[x][y] == '1' or maze[x][y] == 's' or maze[x][y] == 'e' or maze[x][y] in list(self.key_dict.keys()) or maze[x][y] in list(self.key_dict.values())):
            return False
        if (x>0 and x<len(maze)-1):
            if (y>0 and y<len(maze[x])-1):
                if (maze[x-1][y] == '1' or self.is_border(x-1,y,maze)):
                    neighbor_wall_count += 1
                if (maze[x+1][y] == '1' or self.is_border(x+1,y,maze)):
                    neighbor_wall_count += 1
                if (maze[x][y-1] == '1' or self.is_border(x,y-1,maze)):
                    neighbor_wall_count += 1
                if (maze[x][y+1] == '1' or self.is_border(x,y+1,maze)):
                    neighbor_wall_count += 1
        if (neighbor_wall_count>2):
            return True
        else:
            return False
        
    # to find if the square is a border
    def is_border(self, x, y, maze):
        if (x == len(maze) or y == len(maze[x])):
            return True
        return False
    
    # to fill the blocked step as wall
    def fill_dead_end(self, x, y):
        self.grid[x][y] = '1'
        
    def has_dead_end(self, maze):
        for i in range(0, len(maze)):
            for j in range(0, len(maze[i])):
                if self.is_dead_end(i,j,maze):
                    return True
        return False
    
#     def create_path(self):
#         for i in range(0,len(self.grid)):
#             for j in range(0,len(self.grid[i])):
#                 if (len(self.path) == 0):
#                     if (self.grid[i][j] == 's'):
#                         self.start = (i,j)
#                         self.path += (i,j)
                
    
    def next_step(self, x, y):
#         print(self.path)
        up = self.new_grid[x-1][y]
        down = self.new_grid[x+1][y]
        left = self.new_grid[x][y-1]
        right = self.new_grid[x][y+1]
        neighbor_list = [up, down, left, right]
        if (self.new_grid[x][y] == 's'):
            if (len(self.path) == 0):
                self.path.append((x,y))
#                 print(self.path)
                for (a,b) in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
                    if (self.new_grid[a][b] == '0'):
                        self.next_step(a,b)
        elif (self.new_grid[x][y] == 'e'):
            self.path.append((x,y))
            return;
        elif (self.new_grid[x][y] == '0'):
            if (len(self.path) > 0):
                self.path.append((x,y))
                if (neighbor_list.count('0') > 2):
                    print('Junctions' + str((x,y)))
                for (a,b) in ((x,y+1), (x+1,y), (x-1,y), (x,y-1)):
                    if ((self.new_grid[a][b] == '0' or self.new_grid[a][b] == 'e') and (a,b) not in self.path):
                        self.next_step(a,b)
        
    def find_key_door_location(self, key, door, maze):
        key_found = False
        door_found = False
        for i in range(0,len(maze)):
                for j in range(0,len(maze[i])):
                    if (maze[i][j] == key):
                        self.key_location[key] = (i,j)
                        key_found = True
                    if (maze[i][j] == door):
                        self.door_location[door] = (i,j)
                        door_found = True
                    if (key_found and door_found):
                        break
    
    def has_round_path(self, maze):
        for i in range(1,len(maze) - 1):
            for j in range(1,len(maze[0]) - 1):
                if (maze[i][j] == '1'):
                    around_list = [maze[i-1][j-1], maze[i-1][j], maze[i-1][j+1], maze[i][j+1], maze[i+1][j+1], maze[i+1][j], maze[i+1][j-1], maze[i][j-1]]
                    if (around_list.count('1') == 0):
                        print('x,y: ' + str((i,j)))
                        return True
        return False
                        
    def fill_round_path(self, maze):
        
        while (self.has_round_path(maze)):
            for i in range(1,len(maze) - 1):
                for j in range(1,len(maze[0]) - 1):
                    if (maze[i][j] == '1'):
                        around_list = {(i-1,j-1):maze[i-1][j-1], (i-1,j):maze[i-1][j], (i-1,j+1):maze[i-1][j+1], (i,j+1):maze[i][j+1], (i+1,j+1):maze[i+1][j+1], (i+1,j):maze[i+1][j], (i+1,j-1):maze[i+1][j-1], (i,j-1):maze[i][j-1]}
                        if (list(around_list.values()).count('1') == 0):
                            for k,v in around_list.items():
                                keep_cell = False
                                a = k[0]
                                b = k[1]
                                around_list_of_v = {(a-1,b-1):maze[a-1][b-1], (a-1,b):maze[a-1][b], (a-1,b+1):maze[a-1][b+1], (a,b+1):maze[a][b+1], (a+1,b+1):maze[a+1][b+1], (a+1,b):maze[a+1][b], (a+1,b-1):maze[a+1][b-1], (a,b-1):maze[a][b-1]}
                                neighbors = [maze[a-1][b], maze[a][b+1], maze[a+1][b], maze[a][b-1]]
                                for key,val in around_list_of_v.items():
                                    if (val != '1' and key not in list(around_list.keys())):
                                        keep_cell = True
                                        break;
                                if (not keep_cell):
                                    maze[a][b] = '1'
                            
        
    def run(self):
        key_need = {}
        # Find and fill dead-end 1st time
        while (self.has_dead_end(self.grid)):
            for i in range(0,len(self.grid)):
                for j in range(0,len(self.grid[i])):
                    if (self.grid[i][j] == 's'):
                        if not self.start:
                            self.start['x'] = i
                            self.start['y'] = j
                    if (self.is_dead_end(i,j,self.grid)):
                        self.fill_dead_end(i,j)
        self.new_grid = self.grid
        
        # Find and fill round path
        self.fill_round_path(self.new_grid)
        
        # Find and fill dead-end 2nd time
        while (self.has_dead_end(self.new_grid)):
            for i in range(0,len(self.new_grid)):
                for j in range(0,len(self.new_grid[i])):
                    if (self.grid[i][j] == 's'):
                        if not self.start:
                            self.start['x'] = i
                            self.start['y'] = j
                    if (self.is_dead_end(i,j,self.new_grid)):
                        self.fill_dead_end(i,j)
        print(self.key_dict)
        for k,d in self.key_dict.items():
            if any(d in line for line in self.new_grid):
                key_need[d] = k
#         print(key_need)
        for d,k in key_need.items():
            self.find_key_door_location(k,d,self.new_grid)
        print(self.key_location)
        print(self.door_location)
        
        self.next_step(self.start['x'], self.start['y'])
        print("\nMaze after fill dead-end & fill round path")
        print(self.start)
        for line in self.new_grid:
            print(line)
        print(self.path)


# In[16]:


reader = Reader()
reader.read_file("Maze3.txt")
runner = Runner(reader.grid)
# runner.locate_start_end()
runner.run()
# runner.fill_round_path(runner.new_grid)
# for line in runner.new_grid:
#     print(line)


# In[18]:


char = ['a','b','c','d','e','f','g','h','i','s']
doors_keys = {'b':'a', 'd':'c', 'g':'f', 'i':'h'}
doors_list = ['b','d','g','i']
keys_list = []

# Put file path while running
filepath = "Maze2.txt"


# Grid containaing the matrix from the text file
grid = runner.new_grid

# To Be delivered
final_tuple = []


# Step 1

# deep_index(grid, "s")



# Step 2
# Search for index of element in sub-list.
# It will return (x,y)
def deep_index(lst, w):
    for (i, sub) in enumerate(lst):
        if w in sub:
            print("Starting from: " + str(i) + "," + str(sub.index(w)))
            search(i, sub.index(w), 0)



# Step 3
# Read generated grid and search for path
def search(x, y, turn_back):
#     from IPython.core.debugger import set_trace; set_trace()
    # Convert numbers from strings to integers
    if grid[x][y] not in char:
        grid[x][y] = str(grid[x][y])

    # e means the end point
    if grid[x][y] == 'e':
        print('found at %d,%d' % (x, y))
        final_tuple.append((x, y))
        print(final_tuple)

        # Final Grid
        print('')
        for line in grid:
            print(line)
        return True
    
    # 1 means a wall
    elif grid[x][y] == '1':
        #print('Wall at %d,%d' % (x, y))
        return False
        
    # Found a door
    elif grid[x][y] in doors_list:
        print('Found Door: ' + grid[x][y])
        
        need_key = doors_keys[grid[x][y]]
        print('Needed Key: ' + need_key)

        # If we do not have the key
        if need_key not in keys_list:
            a = final_tuple[-1][0]
            b = final_tuple[-1][1]
            search(a, b, 1)
            return False
        else:
            keys_list.remove(need_key)
            print('You can pass')            
            

    # Found a key
    elif grid[x][y] in doors_keys.values():
        keys_list.append(grid[x][y])
        print('Line 80: Visiting %d,%d' % (x, y))
        print('Found Key: ' + grid[x][y])
        final_tuple.append((x,y))
        # Remove the visited path
        grid[x][y] = '9'
        neighbors = {(x-1,y):grid[x-1][y], (x,y+1):grid[x][y+1], (x+1,y):grid[x+1][y], (x,y-1):grid[x][y-1]}
        if (runner.is_dead_end(x, y, grid)): # this means grid[x][y] is a dead-end
            for k,v in neighbors.items():
                if (v == '9'):
                    search(k[0], k[1], 1)
        else:
            if (list(neighbors.values()).count('0') > 0):
                for k,v in neighbors.items():
                    if (v == '0'):
                        search(k[0], k[1], 0)
    
        
    # 9 means already visited
    if grid[x][y] == '9':
        #print('Visited at %d,%d' % (x, y))
        if (turn_back == 1):
            grid[x][y] = '8' # to mark 2nd visit
            if ((x,y) != final_tuple[-1]):
                print('Line 103: Visiting %d,%d' % (x, y))    
                final_tuple.append((x, y))
        else:
            return False
    
    if grid[x][y] == '8':
        neighbors = {(x-1,y):grid[x-1][y], (x,y+1):grid[x][y+1], (x+1,y):grid[x+1][y], (x,y-1):grid[x][y-1]}
        if (turn_back == 1):
#             print((x,y) != final_tuple[-1])
            if ((x,y) != final_tuple[-1]):
#                 print('final[-1]: ' + str(final_tuple[-1]))
#                 print('x,y: ' + str((x,y)))
                print('Line 112: Visiting %d,%d' % (x, y))
                final_tuple.append((x, y))
            if (list(neighbors.values()).count('1') != 1): # this means grid[x][y] is not a junction
                if (list(neighbors.values()).count('0') > 0):
                    for k,v in neighbors.items():
                        if (v == '0'):
                            search(k[0], k[1], 0)
                            return False
                else:
                    for k,v in neighbors.items():
                        if (v == '9' and not runner.is_dead_end(k[0], k[1], grid)):
                            search(k[0], k[1], 1)
                            return False
                        if (v == '8' and (k[0],k[1]) != final_tuple[-2]):
#                             v_neighbors = {(k[0]-1,k[1]):grid[k[0]-1][k[1]], (k[0],k[1]+1):grid[k[0]][k[1]+1], (k[0]+1,k[1]):grid[k[0]+1][k[1]], (k[0],k[1]-1):grid[k[0]][k[1]-1]}
#                             if (list(v_neighbors.values()).count('1') < 2): # this means v is a junction
                            search(k[0], k[1], 1)
                            return False
            else: # grid[x][y] is a junction
                for k,v in neighbors.items():
                    if (v == '8' and (k[0],k[1]) != final_tuple[-2]):
                        search(k[0], k[1], 1)
                        return False
                        
        else:
            return False
                
            
    neighbors = {(x-1,y):grid[x-1][y], (x,y+1):grid[x][y+1], (x+1,y):grid[x+1][y], (x,y-1):grid[x][y-1]}
    # Add to tuple
    if (len(final_tuple) > 0):
#         print((x,y) != final_tuple[-1])
        if ((x,y) != final_tuple[-1]):
#             print('final[-1]: ' + str(final_tuple[-1]))
#             print('x,y: ' + str((x,y)))
            print('Line 142: Visiting %d,%d' % (x, y))    
            final_tuple.append((x, y))
        #print(x, y)
    else:
        print('Line 154: Visiting %d,%d' % (x, y))    
        final_tuple.append((x, y))
    # Mark as visited
    if (turn_back == 0):
        grid[x][y] = '9' # to mark the first visit
#     # If cell is a junction, choose to go straight
#     if (list(neighbors.values()).count('0') > 1 and len(final_tuple) > 1):
#         if (final_tuple[-2][0] == x):
#             des_y = y*2 - final_tuple[-2][1]
#             search(x, des_y, 0)
#         elif (final_tuple[-2][1] == y):
#             des_x = x*2 - final_tuple[-2][0]
#             search(des_x, y, 0)
#         return False     
    
    # Search if neighbor cell is a door
    for k,v in neighbors.items():
        if (v in doors_list and doors_keys[v] in keys_list):
            search(k[0], k[1], 0)
            return False
        
    # Explore paths clockwise starting from the one on the right
#     from IPython.core.debugger import set_trace; set_trace() 
    if ((x < len(grid)-1 and search(x+1, y, 0))
        or (y > 0 and search(x, y-1, 0))
        or (x > 0 and search(x-1, y, 0))
        or (y < len(grid)-1 and search(x, y+1, 0))):
        return True

    return False



#################### STEPS ########################
# Step 1: Read file and generate grid
# read_file(runner.new_grid)
deep_index(grid, "s")

