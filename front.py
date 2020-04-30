"""
EPITA: Maze Runner v0.0.1
Done By:


"""
import pygame
 
 
# Define some colors 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GREY = (132, 141, 149)

 
# This sets the width and height of each cell location
cell_width = 36
cell_height = 36
 
 
# Maze as a 2 dimensional array.
# Or simply a list of lists.
grid = [
['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'], 
['1', 's', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '1'], 
['1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '1', '0', '0', '0', '1', '0', '1'], 
['1', '0', '1', '0', '1', '1', '1', '0', '1', '0', '0', '0', '1', '1', '1', '0', '0', '1'], 
['1', '0', '0', '1', '0', '0', '0', 'i', '0', '1', '1', '0', '1', 'x', '1', 'd', '1', '1'], 
['1', '1', '0', '0', '1', '0', '1', '1', '1', '0', '0', '0', 'x', '2', '1', '0', 'e', '1'], 
['1', '0', '0', '1', '1', '0', '1', '0', 'c', '1', '0', '1', '0', '1', '1', '1', '1', '1'], 
['1', '0', '1', '0', '0', '0', '1', '1', '0', '1', '0', '0', '0', '0', '0', '0', '0', '1'], 
['1', '0', '0', '0', '1', '0', 'b', '0', '0', '1', '0', '1', '1', '1', '1', '0', '1', '1'], 
['1', '1', '0', '1', '1', '0', '1', '0', '1', '0', '1', '0', '0', '0', '1', '0', '0', '1'], 
['1', '0', '0', '1', '0', '0', '1', '0', '1', '0', '1', '0', '1', '0', '0', '1', '0', '1'], 
['1', '0', '1', '1', '0', '1', '0', '0', '0', '0', '0', '0', '1', '1', '0', '1', 'c', '1'], 
['1', '0', '1', '0', '0', '1', '0', '1', '0', '1', '1', '1', '0', '0', '0', '1', '0', '1'], 
['1', '0', '0', '1', '0', '0', 'f', '0', '0', '1', '0', '0', '0', '1', '1', '3', 'x', '1'], 
['1', '1', '0', '1', '1', '1', '0', '1', '0', '1', '0', '1', 'g', '1', '1', 'x', '1', '1'], 
['1', 'a', '0', '1', 'x', 'x', 'x', '4', 'x', 'x', 'x', 'h', '0', '0', '0', 'x', '0', '1'], 
['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1']
]


final_path = [(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (8, 2), (8, 3), (7, 3), (7, 4), (7, 5), (8, 5), (8, 6), (8, 7), (8, 8), (7, 8), (6, 8), (6, 7)]
 

# Initialize pygame
pygame.init()
 
# Set the height and width of the screen
grid_width = cell_width  * len(grid[0])
grid_height = cell_height * len(grid)
grid_size = [grid_width, grid_height]
screen = pygame.display.set_mode(grid_size)

 
# Set title of screen
pygame.display.set_caption("Epita Maze v0.0.1")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()


# Define list of objects that will contain the characters
# characters = []

# block
block = pygame.image.load("resources/sprites/block.png").convert()
block = pygame.transform.scale(block, (cell_width, cell_height))

# blue_door
blue_door = pygame.image.load("resources/sprites/blue_door.png").convert()
blue_door = pygame.transform.scale(blue_door, (cell_width, cell_height))

# blue_key
blue_key = pygame.image.load("resources/sprites/blue_key.png").convert()
blue_key = pygame.transform.scale(blue_key, (cell_width, cell_height))

# ghost
ghost = pygame.image.load("resources/sprites/ghost.png").convert()
ghost = pygame.transform.scale(ghost, (cell_width, cell_height))

# ghost pink cell
ghost_pink_cell = pygame.image.load("resources/sprites/pink_cell.png").convert()
ghost_pink_cell = pygame.transform.scale(ghost_pink_cell, (cell_width, cell_height))

# green_door
green_door = pygame.image.load("resources/sprites/green_door.png").convert()
green_door = pygame.transform.scale(green_door, (cell_width, cell_height))

# green_key
green_key = pygame.image.load("resources/sprites/green_key.png").convert()
green_key = pygame.transform.scale(green_key, (cell_width, cell_height))

# pacman: Start Point
pacman = pygame.image.load("resources/sprites/pacman.png").convert()
pacman = pygame.transform.scale(pacman, (cell_width, cell_height))

# path
path = pygame.image.load("resources/sprites/path.png").convert()
path = pygame.transform.scale(path, (cell_width, cell_height))

# pink_cell
pink_cell = pygame.image.load("resources/sprites/pink_cell.png").convert()
pink_cell = pygame.transform.scale(pink_cell, (cell_width, cell_height))

# red_door
red_door = pygame.image.load("resources/sprites/red_door.png").convert()
red_door = pygame.transform.scale(red_door, (cell_width, cell_height))

# red_key
red_key = pygame.image.load("resources/sprites/red_key.png").convert()
red_key = pygame.transform.scale(red_key, (cell_width, cell_height))

# reward: end point
reward = pygame.image.load("resources/sprites/reward.png").convert()
reward = pygame.transform.scale(reward, (cell_width, cell_height))

# yellow_door
yellow_door = pygame.image.load("resources/sprites/yellow_door.png").convert()
yellow_door = pygame.transform.scale(yellow_door, (cell_width, cell_height))

# yellow_key
yellow_key = pygame.image.load("resources/sprites/yellow_key.png").convert()
yellow_key = pygame.transform.scale(yellow_key, (cell_width, cell_height))


# scale all characters to cell size
#for maze_char in characters:
#    maze_char = pygame.transform.scale(maze_char, (cell_width, cell_height))


 
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
 
    # Set the screen background
    screen.fill(GREY)
 
    # Draw the grid
    for row in range(len(grid)):
        for column in range(len(grid[0])):    
            position_y = row * cell_height
            position_x = column * cell_width


            # path
            if grid[row][column] == '0':
                screen.blit(path, (position_x, position_y))


            # block
            if grid[row][column] == '1':
                screen.blit(block, (position_x, position_y))
            

            # Pacman: Start point
            if grid[row][column] == 's': 
                screen.blit(pacman, (position_x, position_y))
             

            # Reward: End point
            if grid[row][column] == 'e':
                screen.blit(reward, (position_x, position_y))
                

            # Doors
            if grid[row][column] == 'b':
                screen.blit(yellow_door, (position_x, position_y))
            if grid[row][column] == 'c':
                screen.blit(green_door, (position_x, position_y))
            if grid[row][column] == 'g':
                screen.blit(red_door, (position_x, position_y))
            if grid[row][column] == 'i':
                screen.blit(blue_door, (position_x, position_y))

            
            # Keys
            if grid[row][column] == 'a':
                screen.blit(yellow_key, (position_x, position_y))
            if grid[row][column] == 'd':
                screen.blit(green_key, (position_x, position_y))
            if grid[row][column] == 'f':
                screen.blit(red_key, (position_x, position_y))
            if grid[row][column] == 'h':
                screen.blit(blue_key, (position_x, position_y))


            # Ghosts and their paths
            if grid[row][column] == '2' or grid[row][column] == '3' or grid[row][column] == '4':
                screen.blit(ghost, (position_x, position_y))
            if grid[row][column] == 'x':
                screen.blit(ghost_pink_cell, (position_x, position_y))


    # move pacman
    #for i in final_path:
    #    print(i)

    # Limit to 60 frames per second
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()


            
 

# Exit Game (KEEP THIS LINE HERE).
pygame.quit()