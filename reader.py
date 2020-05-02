
# coding: utf-8

# ### Python Week 3-day challenge
# #### Group 23
# #### Students: Anh Tu NGUYEN -  Joseph MERHEB - Sita SHRESTHA

# In[1]:


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
#         from IPython.core.debugger import set_trace; set_trace()
        x0,y0 = p1
        x1,y1 = p2
        
        # difference between x1 and x0
        dx = abs(x1 - x0)
        # difference between y1 and y0
        dy = abs(y1 - y0)
        x = x0
        y = y0
        
        # increment of x and y
        x_incre = 0
        y_incre = 0
        
        # if x1 > x0, move 1 cell down, else move 1 cell up
        if (x1 > x0):
            x_incre = 1
        else:
            x_incre = -1
            
        # if y1 > y0, move 1 cell right, else move 1 cell left
        if (y1 > y0):
            y_incre = 1
        else:
            y_incre = -1
        
        # different between number of vertical cells and horizontal cells
        diff = dx - dy
        # number of cells expected to pass
        n = 1 + dx + dy
        dx *= 2
        dy *= 2
        result = []

        for i in range(0,n):
            # if there are more vertical cells than horizontal cells, move 1 cell vertically
            if diff > 0:
                x += x_incre
                diff -= dy
            
            # if there are more horizontal cells than vertical cells, move 1 cell horizontally
            elif diff < 0:
                y += y_incre
                diff += dx
            
            # if vertical cells = horizontal cells, it means the line is a perfect diagonal line
            elif diff == 0:
                x += x_incre
                y += y_incre
                diff -= dy
                diff += dx
            result.append((x,y))
            if (x,y) == (x1,y1): 
                break
        return result
    
    # to check if cell is seen by the ghost
    def is_blocked_from_ghost(self, cell_pos, ghost_pos, maze):
        a,b = cell_pos
        x,y = ghost_pos
        # if cell is at top-left of ghost
        if (a < x and b < y):
            # if there are walls at top-left of ghost
            if (maze[x-1][y] == WALL and maze[x][y-1] == WALL):
                return True
        # if cell is at top-right of ghost
        elif (a < x and b > y):
            # if there are walls at top-right of ghost
            if (maze[x-1][y] == WALL and maze[x][y+1] == WALL):
                return True
        # if cell is at bottom-right of ghost
        elif (a > x and b > y):
            # if there are walls at bottom-right of ghost
            if (maze[x+1][y] == WALL and maze[x][y+1] == WALL):
                return True
        # if cell is at bottom-left of ghost
        elif (a > x and b < y):
            # if there are walls at bottom-left of ghost
            if (maze[x+1][y] == WALL and maze[x][y-1] == WALL):
                return True
        for (i,j) in self.ray_trace(cell_pos, ghost_pos):
            if (maze[i][j] == WALL):
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
                    if (maze[x+i][y+j] == WALL):
                        continue
                    elif self.is_blocked_from_ghost((x+i,y+j), (x,y), maze):
                        continue
                    else:
                        maze[x+i][y+j] = GHOST_RANGE
    
    # read the input file
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
            
        return self.grid

