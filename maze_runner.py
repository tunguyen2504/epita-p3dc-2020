
# coding: utf-8

# ### Python Week 3-day challenge
# #### Group 23
# #### Students: Anh Tu NGUYEN -  Joseph MERHEB - Sita SHRESTHA

# In[56]:


# Class to read a maze from a file
class Reader:
    def __init__(self):
        self.grid = []
            
    # to find if it is a ghost
    def is_ghost(self, x, y, maze):
        if (maze[x][y].isdigit() and int(maze[x][y]) > 1):
            return True
        
    # to find the lines of sight between 2 cell
    def ray_trace(self,p1,p2):
        x0,y0 = p1
        x1,y1 = p2

        dx = abs(x1 - x0)
        dy = abs(y1 - y0)
        x = x0
        y = y0

        x_incre = 0
        y_incre = 0
        if (x1 > x0):
            x_incre = 1
        else:
            x_incre = -1
        if (y1 > y0):
            y_incre = 1
        else:
            y_incre = -1
        error = dx - dy
        n = 1 + dx + dy
        dx *= 2
        dy *= 2
#         print('n: ' + str(n))
#         print('dx: ' + str(dx))
#         print('dy: ' + str(dy))
#         print('error: ' + str(error))
        result = []

        for i in range(0,n):
            if error > 0:
                x += x_incre
                error -= dy

            elif error < 0:
                y += y_incre
                error += dx

            elif error == 0:
                x += x_incre
                y += y_incre
                error -= dy
                error += dx
            result.append((x,y))
#             print((x,y))
#             print(error)
            if (x,y) == (x1,y1): break
        return result
    
    # to check if cell is seen by the ghost
    def is_blocked_from_ghost(self, cell_pos, ghost_pos, maze):
        a,b = cell_pos
        x,y = ghost_pos
        # if cell is at top-left of ghost
        if (a < x and b < y):
            if (maze[x-1][y] == '1' and maze[x][y-1] == '1'):
                return True
        # if cell is at top-right of ghost
        elif (a < x and b > y):
            if (maze[x-1][y] == '1' and maze[x][y+1] == '1'):
                return True
        # if cell is at bottom-right of ghost
        elif (a > x and b > y):
            if (maze[x+1][y] == '1' and maze[x][y+1] == '1'):
                return True
        # if cell is at bottom-left of ghost
        elif (a > x and b < y):
            if (maze[x+1][y] == '1' and maze[x][y-1] == '1'):
                return True
        for (i,j) in self.ray_trace(cell_pos, ghost_pos):
            if (maze[i][j] == '1'):
                return True
        return False
    
    # to fill the range around the ghost
    def fill_ghost_range(self, x, y, maze):
        g_range = int(maze[x][y]) - 1
        # In the square that around the ghost, with range equal to ghost number - 1
        for i in range(-g_range, g_range+1):
            for j in range(-g_range, g_range+1):
                # To ensure that maze[i][j] exists and maze[i][j] is not the ghost
                if (x+i > 0 and x+i < (len(maze) - 1) and y+j > 0 and y+j < (len(maze[x]) - 1) and (i,j) != (0,0)):
                    if (maze[x+i][y+j] == '1'):
                        continue
                    elif self.is_blocked_from_ghost((x+i,y+j), (x,y), maze):
                        continue
                    else:
                        maze[x+i][y+j] = 'x'
    
    def read_file(self, file_path):
        with open(file_path, 'r') as my_txt:        
            # For each line     
            lines = my_txt.read().splitlines()
            for line in lines:
                line = line.split(" ")
                if (len(line) > len(lines[0].split(" "))):
                    del line[-1]
                self.grid.append(line)
        
#         from IPython.core.debugger import set_trace; set_trace()
        for i in range(0,len(self.grid)):
            for j in range(0,len(self.grid[i])):
                if self.is_ghost(i, j, self.grid):
                    self.fill_ghost_range(i, j, self.grid)
        
        print("------------- THE MAZE -------------")
        for line in self.grid:
            print(line)


# In[57]:


# Class to find output for the maze
class Runner:
    def __init__(self, grid):
        self.grid = grid
        self.new_grid = []
        self.start = {}
        self.final_tuple = []
        self.doors_keys = {'b':'a', 'c':'d', 'g':'f', 'i':'h'}
        self.keys_list = []
        
    # to find if the step is blocked
    def is_dead_end(self, x, y, maze):
        neighbor_wall_count = 0
        if (maze[x][y] == '1' or maze[x][y] == 's' or maze[x][y] == 'e' or reader.is_ghost(x, y, maze) or maze[x][y] == 'x' or maze[x][y] in list(self.doors_keys.keys()) or maze[x][y] in list(self.doors_keys.values())):
            return False
        if (x>0 and x<len(maze)-1):
            if (y>0 and y<len(maze[x])-1):
                if (maze[x-1][y] == '1' or maze[x-1][y] == 'x' or self.is_border(x-1,y,maze)):
                    neighbor_wall_count += 1
                if (maze[x+1][y] == '1' or maze[x+1][y] == 'x' or self.is_border(x+1,y,maze)):
                    neighbor_wall_count += 1
                if (maze[x][y-1] == '1' or maze[x][y-1] == 'x' or self.is_border(x,y-1,maze)):
                    neighbor_wall_count += 1
                if (maze[x][y+1] == '1' or maze[x][y+1] == 'x' or self.is_border(x,y+1,maze)):
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
    def fill_dead_end(self, x, y, maze):
        maze[x][y] = '1'
       
    # to find if there is a dead-end cell in the maze
    def has_dead_end(self, maze):
        for i in range(0, len(maze)):
            for j in range(0, len(maze[i])):
                if self.is_dead_end(i,j,maze):
                    return True
        return False
    
    # to find if there is a round-path in the maze
    def has_round_path(self, maze):
        for i in range(1,len(maze) - 1):
            for j in range(1,len(maze[0]) - 1):
                if (maze[i][j] == '1'):
                    around_list = [maze[i-1][j-1], maze[i-1][j], maze[i-1][j+1], maze[i][j+1], maze[i+1][j+1], maze[i+1][j], maze[i+1][j-1], maze[i][j-1]]
                    if (around_list.count('1') == 0):
                        return True
        return False

    # to fill the round-path
    def fill_round_path(self, maze):
        while (self.has_round_path(maze)):
            for i in range(1,len(maze) - 1):
                for j in range(1,len(maze[0]) - 1):
                    if (maze[i][j] == '1'):
                        around_list = {(i-1,j-1):maze[i-1][j-1], (i-1,j):maze[i-1][j], (i-1,j+1):maze[i-1][j+1], (i,j+1):maze[i][j+1], (i+1,j+1):maze[i+1][j+1], (i+1,j):maze[i+1][j], (i+1,j-1):maze[i+1][j-1], (i,j-1):maze[i][j-1]}
                        if (list(around_list.values()).count('1') == 0):
                            for k,v in around_list.items():
                                keep_cell = False
                                if (v in self.doors_keys.keys() or v in self.doors_keys.values()):
                                    continue
                                else:
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
                
                                    
    def search(self, maze, x, y, turn_back):
#     from IPython.core.debugger import set_trace; set_trace()
        # e means the end point
        if maze[x][y] == 'e':
#             print('Exit at %d,%d' % (x, y))
            self.final_tuple.append((x, y))
            print("\n Path to exit:")
            print(self.final_tuple)

            # Final Maze
#             print('')
#             for line in maze:
#                 print(line)
            return True

        # 1 means a wall
        elif maze[x][y] == '1':
#             print('Wall at %d,%d' % (x, y))
            return False

        # 'x' means sight of the ghost
        elif maze[x][y] == 'x':
            return False

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
    #         from IPython.core.debugger import set_trace; set_trace()
            self.keys_list.append(maze[x][y])
#             print('Line 118: Visiting %d,%d' % (x, y))
#             print('Found Key: ' + maze[x][y])
            self.final_tuple.append((x,y))
            # Mark the first visit
            maze[x][y] = '*'
            # 4 neighbor cells
            neighbors = {(x-1,y):maze[x-1][y], (x,y+1):maze[x][y+1], (x+1,y):maze[x+1][y], (x,y-1):maze[x][y-1]}
            if (self.is_dead_end(x, y, maze)): # this means maze[x][y] is a dead-end
                # Fill cell to be wall
                self.fill_dead_end(x, y, maze)
                # Find the way to go back
                for k,v in neighbors.items():
                    if (v == '*'):
                        self.search(maze, k[0], k[1], 1)
                return False
            else:
                # if there is cell that has not been visited, then visit it
                if (list(neighbors.values()).count('0') > 0):
                    for k,v in neighbors.items():
                        if (v == '0'):
                            self.search(maze, k[0], k[1], 0)
                return False


        # '*' means visited once
        if maze[x][y] == '*':
            if (turn_back == 1):
                # Mark the second visit
                maze[x][y] = '@' 
                if ((x,y) != self.final_tuple[-1]):
#                     print('Line 148: Visiting %d,%d' % (x, y))    
                    self.final_tuple.append((x, y))
            else:
                # Fill cell to be wall if cell is a dead-end
                if (self.is_dead_end(x, y, maze)):
                    self.fill_dead_end(x, y, maze)
                return False

        # '@' means visited twice 
        if maze[x][y] == '@':
            neighbors = {(x-1,y):maze[x-1][y], (x,y+1):maze[x][y+1], (x+1,y):maze[x+1][y], (x,y-1):maze[x][y-1]}
            if (turn_back == 1):
                # Fill cell to be wall if cell is a dead-end
                if (self.is_dead_end(x, y, maze)):
                    self.fill_dead_end(x, y, maze)

                if ((x,y) != self.final_tuple[-1]):
#                     print('Line 165: Visiting %d,%d' % (x, y))
                    self.final_tuple.append((x, y))
                    # Fill cell to be wall if cell is a dead-end
                    if (self.is_dead_end(x, y, maze)):
                        self.fill_dead_end(x, y, maze)

                # This means maze[x][y] is not a junction
                if (list(neighbors.values()).count('1') != 1):
                    # if there is cell that has not been visited, then visit it
                    if (list(neighbors.values()).count('0') > 0):
                        for k,v in neighbors.items():
                            if (v == '0'):
                                self.search(maze, k[0], k[1], 0)
                                return False
                    else:
                        for k,v in neighbors.items():
                            if (v == '*'):
                                self.search(maze, k[0], k[1], 1)
                                return False
                            if (v == '@' and (k[0],k[1]) != self.final_tuple[-2]):
                                self.search(maze, k[0], k[1], 1)
                                return False
                # else maze[x][y] is a junction
                else: 
                    for k,v in neighbors.items():
                        if (v == '@' and (k[0],k[1]) != self.final_tuple[-2]):
                            self.search(maze, k[0], k[1], 1)
                            return False

            else:
                return False


        neighbors = {(x-1,y):maze[x-1][y], (x,y+1):maze[x][y+1], (x+1,y):maze[x+1][y], (x,y-1):maze[x][y-1]}
        # Add to tuple
        if (len(self.final_tuple) > 0):
            if ((x,y) != self.final_tuple[-1]):
#                 print('Line 202: Visiting %d,%d' % (x, y))    
                self.final_tuple.append((x, y))
        else:
#             print('Line 205: Visiting %d,%d' % (x, y))    
            self.final_tuple.append((x, y))

        # Mark as visited
        if (turn_back == 0):
            maze[x][y] = '*' # to mark the first visit
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
#                     elif (self.is_ghost(i,j,self.grid)):
                        
                    elif (self.is_dead_end(i,j,self.grid)):
                        self.fill_dead_end(i,j,self.grid)
                    
        self.new_grid = self.grid
        
        # Find and fill round path
#         self.fill_round_path(self.new_grid)
        
        # Find and fill dead-end 2nd time
#         while (self.has_dead_end(self.new_grid)):
#             for i in range(0,len(self.new_grid)):
#                 for j in range(0,len(self.new_grid[i])):
#                     if (self.grid[i][j] == 's'):
#                         if not self.start:
#                             self.start['x'] = i
#                             self.start['y'] = j
#                     if (self.is_dead_end(i,j,self.new_grid)):
#                         self.fill_dead_end(i,j,self.grid)
        
        print("\nMaze after fill dead-end & fill round path")
        print(self.start)
        for line in self.new_grid:
            print(line)
        
        # Start searching
        self.search(self.new_grid, self.start['x'], self.start['y'], 0)


# In[58]:


# import argparse
# def main():
#     parser = argparse.ArgumentParser()
#     parser.add_argument("input", type=str)

#     args = parser.parse_args()

#     reader = Reader()
#     reader.read_file(args.input)
#     runner = Runner(reader.grid)
#     runner.run()
    
# if __name__ == "__main__":
#     main()
    
reader = Reader()
reader.read_file("Maze4.txt")
runner = Runner(reader.grid)
runner.run()

