
# coding: utf-8

# ### Python Week 3-day challenge
# #### Group 23
# #### Students: Anh Tu NGUYEN -  Joseph MERHEB - Sita SHRESTHA

# In[1]:


WALL = '1'
GHOST_RANGE = 'x'
CELL = '0'
START = 's'
END = 'e'
VISITED_ONCE = '*'
VISITED_TWICE = '@'


# In[6]:


# Class to find output for the maze
class Runner:
    def __init__(self, grid):
        self.grid = grid
        self.new_grid = []
        self.start = {}
        self.final_tuple = []
        self.doors_keys = {'b':'a', 'c':'d', 'g':'f', 'i':'h'}
        self.keys_list = []
        self.round_paths = {}
        self.round_path_exits = {}
        
    # to find if the step is blocked
    def is_dead_end(self, x, y, maze):
        r = Reader()
        neighbor_wall_count = 0
        if (maze[x][y] == WALL or maze[x][y] == START or maze[x][y] == END or maze[x][y] in list(self.doors_keys.keys()) or maze[x][y] in list(self.doors_keys.values())):
            return False
        if (r.is_ghost(x, y, maze) or maze[x][y] == GHOST_RANGE):
            return True
        if (x>0 and x<len(maze)-1):
            if (y>0 and y<len(maze[x])-1):
                if (maze[x-1][y] == WALL or maze[x-1][y] == GHOST_RANGE or self.is_border(x-1,y,maze)):
                    neighbor_wall_count += 1
                if (maze[x+1][y] == WALL or maze[x+1][y] == GHOST_RANGE or self.is_border(x+1,y,maze)):
                    neighbor_wall_count += 1
                if (maze[x][y-1] == WALL or maze[x][y-1] == GHOST_RANGE or self.is_border(x,y-1,maze)):
                    neighbor_wall_count += 1
                if (maze[x][y+1] == WALL or maze[x][y+1] == GHOST_RANGE or self.is_border(x,y+1,maze)):
                    neighbor_wall_count += 1
        if (neighbor_wall_count>2):
            return True
        else:
            return False
        
    # to find if the cell is a border
    def is_border(self, x, y, maze):
        if (x == 0 or x == len(maze) or y == 0 or y == len(maze[x])):
            return True
        return False
    
    # to fill the blocked step as wall
    def fill_dead_end(self, x, y, maze):
        maze[x][y] = WALL
       
    # to find if there is a dead-end cell in the maze (surrounded by walls)
    def has_dead_end(self, maze):
        for i in range(0, len(maze)):
            for j in range(0, len(maze[i])):
                if self.is_dead_end(i,j,maze):
                    return True
        return False
    
    # to find if there is a round-path in the maze
    def find_round_path(self, maze):
        for x in range(1,len(maze) - 1):
            for y in range(1,len(maze[0]) - 1):
                # if cell is a wall, try to check if around it is a path or not
                if (maze[x][y] == WALL):
                    around_list = {}
                    for i in range(-1,2):
                        for j in range(-1,2):
                            # To ensure that maze[i][j] exists and maze[i][j] is not the wall
                            if (x+i >= 0 and x+i < (len(maze)) and y+j >= 0 and y+j < (len(maze[x])) and (i,j) != (0,0)):
                                around_list[(x+i,y+j)] = maze[x+i][y+j]
                    if (list(around_list.values()).count(WALL) == 0):
                        self.round_paths[(x,y)] = list(around_list.keys())
                        exit_cells = []
                        for (a,b) in around_list.keys():
                            key_neighbor = [(a-1,b), (a,b+1), (a+1,b), (a,b-1)]
                            for (x0,y0) in key_neighbor:
                                if (maze[x0][y0] != WALL and maze[x0][y0] != GHOST_RANGE and (x0,y0) not in around_list.keys()):
                                    exit_cells.append((a,b))
                                    break
                        self.round_path_exits[(x,y)] = exit_cells

    # check if there is a key in round_path
    def is_key_in_round_path(self, center_pos, maze):
        cell_list = self.round_paths[center_pos]
        for (x,y) in cell_list:
            if (maze[x][y] in self.doors_keys.values()):
                return True
        return False
    
    # check if pacman has entered a round path, if yes return center position
    def check_round_path(self, curr_pos, maze):
        for center, cell_list in self.round_paths.items():
            if (curr_pos in cell_list):
                return center
        return None
    
    # find way to exit a round path:
    # curr_pos: current position
    # center: the center wall
    def exit_round_path(self, curr_pos, center, maze):
        r = Reader()
        # the cell at the exit of the round path
        exit_pos = ()
        # for each cell in the way out
        for cell in self.round_path_exits[center]:
            if (curr_pos != cell):
                exit_pos = cell
        (x,y) = curr_pos
        path = [(x,y)]
        
        # the result path if there is no block
        path = path + r.ray_trace(curr_pos, exit_pos)
        for (x0,y0) in path:
            # if there is block in the path, we have to avoid it
            if maze[x0][y0] == WALL:
                exit_path = [(x,y)]
                if (x0 == x):
                    exit_path = exit_path + r.ray_trace(curr_pos, (exit_pos[0],y)) + r.ray_trace((exit_pos[0],y), exit_pos)
                elif (y0 == y):
                    exit_path = exit_path + r.ray_trace(curr_pos, (x,exit_pos[1])) + r.ray_trace((x,exit_pos[1]), exit_pos)
                else:
                    exit_path = exit_path + r.ray_trace(curr_pos, (exit_pos[0],y)) + r.ray_trace((exit_pos[0],y),exit_pos)
                return exit_path
        return path
                
    # search for maze[x][y], turn_back to indicate the step is new visit or 2nd visit                                
    def search(self, maze, x, y, turn_back):
#         if (x,y) == (11,8):
#             from IPython.core.debugger import set_trace; set_trace()
        
        # 1 means a wall
        if maze[x][y] == WALL:
            return False

        # GHOST_RANGE means sight of the ghost
        elif maze[x][y] == GHOST_RANGE:
            return False
            
        # Check if key found is in any round path, then fill the round path
        elif self.check_round_path((x,y), maze) is None:
            for center, cells in self.round_paths.items():
                # if there is no more key on the round path, then clear it
                if not self.is_key_in_round_path(center, maze):
                    start_cell = self.round_path_exits[center][0]
                    exit_path = self.exit_round_path(start_cell, center, maze)
                    for cell in exit_path:
                        if cell in self.round_paths[center]:
                            self.round_paths[center].remove(cell)
                    for (xc,yc) in self.round_paths[center]:
                        self.fill_dead_end(xc, yc, self.grid)
    
        # e means the end point
        if maze[x][y] == END:
#             print('Exit at %d,%d' % (x, y))
            self.final_tuple.append((x, y))
            print("\n Path to exit:")
            print(self.final_tuple)

            # Final Maze
#             print('')
#             for line in maze:
#                 print(line)
            return True

        # Found a door
        elif maze[x][y] in self.doors_keys.keys():
#             print('Found Door: ' + maze[x][y])

            need_key = self.doors_keys[maze[x][y]]
#             print('Needed Key: ' + need_key)

            # If we do not have the key
            if need_key not in self.keys_list:
                a = self.final_tuple[-1][0]
                b = self.final_tuple[-1][1]
                # Go back to previous cell
                self.search(maze, a, b, 1)
                return False
            else:
                # Open the door and lose the key
                self.keys_list.remove(need_key)
#                 print('You can pass')


        # Found a key
        elif maze[x][y] in self.doors_keys.values():
            self.keys_list.append(maze[x][y])
#             print('Line 209: Visiting %d,%d' % (x, y))
#             print('Found Key: ' + maze[x][y])
            self.final_tuple.append((x,y))
            
            # Mark the first visit
            maze[x][y] = VISITED_ONCE   
            
            # 4 neighbor cells
            neighbors = {(x-1,y):maze[x-1][y], (x,y+1):maze[x][y+1], (x+1,y):maze[x+1][y], (x,y-1):maze[x][y-1]}
            if (self.is_dead_end(x, y, maze)): # this means maze[x][y] is a dead-end
                # Fill cell to be wall
                self.fill_dead_end(x, y, maze)
                # Find the way to go back
                for k,v in neighbors.items():
                    if (v == VISITED_ONCE):
                        self.search(maze, k[0], k[1], 1)
                return False
            else:
                # if there is cell that has not been visited, then visit it
                if (list(neighbors.values()).count(CELL) > 0):
                    for k,v in neighbors.items():
                        if (v == CELL):
                            self.search(maze, k[0], k[1], 0)
                return False


        # if cell is visited once
        if maze[x][y] == VISITED_ONCE:
            if (turn_back == 1):
                # Mark the second visit
                maze[x][y] = VISITED_TWICE 
                if ((x,y) != self.final_tuple[-1]):
#                     print('Line 241: Visiting %d,%d' % (x, y))    
                    self.final_tuple.append((x, y))
            else:
                # Fill cell to be wall if cell is a dead-end
                if (self.is_dead_end(x, y, maze)):
                    self.fill_dead_end(x, y, maze)
                return False

        # if cell is visited twice or more
        if maze[x][y] == VISITED_TWICE:
            neighbors = {(x-1,y):maze[x-1][y], (x,y+1):maze[x][y+1], (x+1,y):maze[x+1][y], (x,y-1):maze[x][y-1]}
            if (turn_back == 1):
                # Fill cell to be wall if cell is a dead-end
                if (self.is_dead_end(x, y, maze)):
                    self.fill_dead_end(x, y, maze)

                if ((x,y) != self.final_tuple[-1]):
#                     print('Line 258: Visiting %d,%d' % (x, y))
                    self.final_tuple.append((x, y))
                    
                    # Fill cell to be wall if cell is a dead-end
                    if (self.is_dead_end(x, y, maze)):
                        self.fill_dead_end(x, y, maze)

                # This means maze[x][y] is not a junction
                if (list(neighbors.values()).count(WALL) != 1):
                    # if there is cell that has not been visited, then visit it
                    if (list(neighbors.values()).count(CELL) > 0):
                        for k,v in neighbors.items():
                            if (v == CELL):
#                                 from IPython.core.debugger import set_trace; set_trace() 
                                self.search(maze, k[0], k[1], 0)
                                return False
                    else:
                        for k,v in neighbors.items():
                            if (v == VISITED_ONCE):
                                self.search(maze, k[0], k[1], 1)
                                return False
                            if (v == VISITED_TWICE and (k[0],k[1]) != self.final_tuple[-2]):
                                self.search(maze, k[0], k[1], 1)
                                return False
                # else maze[x][y] is a junction
                else: 
                    for k,v in neighbors.items():
                        if ((v == VISITED_TWICE or v == VISITED_ONCE) and (k[0],k[1]) != self.final_tuple[-2]):
                            self.search(maze, k[0], k[1], 1)
                            return False

            else:
                return False


        neighbors = {(x-1,y):maze[x-1][y], (x,y+1):maze[x][y+1], (x+1,y):maze[x+1][y], (x,y-1):maze[x][y-1]}
        
        # Add to tuple
        if (len(self.final_tuple) > 0):
            if ((x,y) != self.final_tuple[-1]):
#                 print('Line 296: Visiting %d,%d' % (x, y))    
                self.final_tuple.append((x, y))
        else:
#             print('Line 299: Visiting %d,%d' % (x, y))
            self.final_tuple.append((x, y))

        # Mark as visited
        if (turn_back == 0):
            # Mark the first visit
            maze[x][y] = VISITED_ONCE
                    
            if (self.is_dead_end(x, y, maze)):
                self.fill_dead_end(x, y, maze)

        # Search if neighbor cell is a door, if exist, visit the door first
        for k,v in neighbors.items():
            if (v in self.doors_keys.keys() and self.doors_keys[v] in self.keys_list):
                self.search(maze, k[0], k[1], 0)
                return False

        # Explore paths clockwise starting from the one on the right
#         from IPython.core.debugger import set_trace; set_trace() 
        if ((x < len(maze)-1 and self.search(maze, x+1, y, 0))
            or (y > 0 and self.search(maze, x, y-1, 0))
            or (x > 0 and self.search(maze, x-1, y, 0))
            or (y < len(maze)-1 and self.search(maze, x, y+1, 0))):
            return True

        return False                          
        
    # Pacman start
    def run(self):
        key_need = {}
        # Find and fill dead-end cells
        while (self.has_dead_end(self.grid)):
            for i in range(0,len(self.grid)):
                for j in range(0,len(self.grid[i])):
                    if (self.grid[i][j] == START):
                        if not self.start:
                            self.start[GHOST_RANGE] = i
                            self.start['y'] = j
                    elif (self.is_dead_end(i,j,self.grid)):
                        self.fill_dead_end(i,j,self.grid)
                    
        self.new_grid = self.grid
        
        # Find all round path
        self.find_round_path(self.new_grid)
        
        # Fill round path if there is no key inside
        for center, round_path in self.round_paths.items():
            if not self.is_key_in_round_path(center, self.new_grid):
                start_round = self.round_path_exits[center][0]
                exit_path = self.exit_round_path(start_round, center, self.new_grid)
                
                # Remove cell used to run
                for cell in exit_path:
                    if cell in self.round_paths[center]:
                        self.round_paths[center].remove(cell)
                
                # Fill all the unnecessary cells to be wall
                for (x,y) in self.round_paths[center]:
                    self.fill_dead_end(x, y, self.grid)
        
#         print("\nMaze after fill dead-end & fill round path")
#         print(self.start)
#         for line in self.new_grid:
#             print(line)
        
        # Start searching
        self.search(self.new_grid, self.start[GHOST_RANGE], self.start['y'], 0)
        
        return self.final_tuple


# In[7]:


import argparse
from reader import *
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=str)

    args = parser.parse_args()

    reader = Reader()
    maze = reader.read_file(args.input)
    runner = Runner(maze)
    runner.run()
    
if __name__ == "__main__":
    main()
    
# reader = Reader()
# reader.read_file("Maze4.txt")
# runner = Runner(reader.grid)
# runner.run()

