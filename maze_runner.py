
# coding: utf-8

# In[22]:


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
        for line in self.grid:
            print(line)


# In[29]:


class Runner:
    def __init__(self, grid):
        self.grid = grid
        self.start = ()
        self.end = ()
        self.path = []
        
    # to locate the start position
    def locate_start_end(self, pos, i, j):
        if (pos == 's'):
            self.start = (i,j)
        elif (pos == 'e'):
            self.start = (i,j)
        
    # to find if the step is blocked
    def is_dead_end(self, x, y):
        neighbor_wall_count = 0
        if (self.grid[x][y] == '1'):
            return False
        if (x>0 and x<len(self.grid)-1):
            if (y>0 and y<len(self.grid[x])-1):
                if (self.grid[x-1][y] == '1'):
                    neighbor_wall_count += 1
                if (self.grid[x+1][y] == '1'):
                    neighbor_wall_count += 1
                if (self.grid[x][y-1] == '1'):
                    neighbor_wall_count += 1
                if (self.grid[x][y+1] == '1'):
                    neighbor_wall_count += 1
        if (neighbor_wall_count>2):
            return True
        else:
            return False
    
    # to fill the blocked step as wall
    def fill_dead_end(self, x, y):
        self.grid[x][y] = '1'
        
    def has_dead_end(self, maze):
        for i in range(0, len(maze)):
            for j in range(0, len(maze[i])):
                if self.is_dead_end(i,j):
                    return True
        return False
    
    def run(self):
        while (self.has_dead_end(self.grid)):
            for i in range(0,len(self.grid)):
                for j in range(0,len(self.grid[i])):
                    if (self.grid[i][j] == 's' or self.grid[i][j] == 'e'):
                        continue
                    if (self.is_dead_end(i,j)):
                        self.fill_dead_end(i,j)
        for line in self.grid:
            print(line)


# In[ ]:


reader = Reader()
reader.read_file("maze1.txt")
runner = Runner(reader.grid)
# runner.locate_start_end()
runner.run()

