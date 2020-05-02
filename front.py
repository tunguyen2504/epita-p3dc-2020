"""
EPITA: Maze Runner v0.0.1
Done By: Group 23
Students: Anh Tu NGUYEN -  Joseph MERHEB - Sita SHRESTHA
"""

import pygame
#from .dir import Reader


# Settings
cell_width = 36
cell_height = 36

# Waiting time at the end
WAITING_TIME = 3000

# Pacman speed. Fames/second
PACMAN_SPEED = 5

# Constants
WALL = '1'
GHOST_RANGE = 'x'
CELL = '0'
START = 's'
END = 'e'
VISITED_ONCE = '*'
VISITED_TWICE = '@'

YELLOW_KEY = 'a'
YELLOW_DOOR = 'b'
GREEN_DOOR = 'c'
GREEN_KEY = 'd'
RED_KEY = 'f'
RED_DOOR = 'g'
BLUE_KEY = 'h'
BLUE_DOOR = 'i'
 
# Maze as a 2 dimensional array (List of lists)
grid = [
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
    ['1', 's', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '1'],
    ['1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '1', '0', '0', '0', '1', '0', '1'],
    ['1', '0', '1', '0', '1', '1', '1', '0', '1', '0', '0', '0', '1', '1', '1', '0', '0', '1'],
    ['1', '0', '0', '1', '0', '0', '0', 'i', '0', '1', '1', '0', '1', 'x', '1', 'c', '1', '1'],
    ['1', '1', '0', '0', '1', '0', '1', '1', '1', '0', '0', '0', 'x', '2', '1', '0', 'e', '1'],
    ['1', '0', '0', '1', '1', '0', '1', '0', '0', '1', '0', '1', 'x', '1', '1', '1', '1', '1'],
    ['1', '0', '1', '0', '0', '0', '1', '1', '0', '1', '0', '0', '0', '0', '0', '0', '0', '1'],
    ['1', '0', '0', '0', '1', '0', 'b', '0', '0', '1', '0', '1', '1', '1', '1', '0', '1', '1'],
    ['1', '1', '0', '1', '1', '0', '1', '0', '1', '0', '1', '0', '0', '0', '1', '0', '0', '1'],
    ['1', '0', '0', '1', '0', '0', '1', '0', '1', '0', '1', '0', '1', '0', '0', '1', '0', '1'],
    ['1', '0', '1', '1', '0', '1', '0', '0', '0', '0', '0', '0', '1', '1', '0', '1', 'd', '1'],
    ['1', '0', '1', '0', 'x', '1', '0', '1', '0', '1', '1', '1', '0', '0', '0', '1', 'x', '1'],
    ['1', '0', '0', '1', '0', 'x', 'f', '0', '0', '1', '0', '0', '0', '1', '1', '3', 'x', '1'],
    ['1', '1', '0', '1', '1', '1', 'x', '1', 'x', '1', '0', '1', 'g', '1', '1', 'x', '1', '1'],
    ['1', 'a', '0', '1', 'x', 'x', 'x', '4', 'x', 'x', 'x', 'h', '0', '0', '0', 'x', '0', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1']
]


# Path
# Maze 4
final_path = [(1, 1), (2, 1), (3, 1), (4, 1), (4, 2), (5, 2), (6, 2), (6, 1), (7, 1), (8, 1), (8, 2), (9, 2), (10, 2), (10, 1), (11, 1), (12, 1), (13, 1), (13, 2), (14, 2), (15, 2), (15, 1), (15, 2), (14, 2), (13, 2), (13, 1), (12, 1), (11, 1), (10, 1), (10, 2), (9, 2), (8, 2), (8, 3), (7, 3), (7, 4), (7, 5), (8, 5), (8, 6), (8, 7), (9, 7), (10, 7), (11, 7), (11, 6), (12, 6), (13, 6), (13, 7), (13, 8), (12, 8), (11, 8), (11, 9), (11, 10), (11, 11), (10, 11), (9, 11), (9, 12), (9, 13), (10, 13), (10, 14), (11, 14), (12, 14), (12, 13), (12, 12), (13, 12), (14, 12), (15, 12), (15, 11), (15, 12), (14, 12), (13, 12), (12, 12), (12, 13), (12, 14), (11, 14), (10, 14), (10, 13), (9, 13), (9, 12), (9, 11), (10, 11), (11, 11), (11, 10), (11, 9), (11, 8), (11, 7), (10, 7), (9, 7), (8, 7), (8, 6), (8, 5), (7, 5), (6, 5), (5, 5), (4, 5), (4, 6), (4, 7), (3, 7), (2, 7), (1, 7), (1, 8), (1, 9), (2, 9), (3, 9), (3, 10), (3, 11), (4, 11), (5, 11), (5, 10), (6, 10), (7, 10), (7, 11), (7, 12), (7, 13), (7, 14), (7, 15), (8, 15), (9, 15), (9, 16), (10, 16), (11, 16), (10, 16), (9, 16), (9, 15), (8, 15), (7, 15), (7, 14), (7, 13), (7, 12), (7, 11), (7, 10), (6, 10), (5, 10), (5, 11), (4, 11), (3, 11), (3, 10), (3, 9), (2, 9), (1, 9), (1, 10), (1, 11), (1, 12), (2, 12), (2, 13), (2, 14), (1, 14), (1, 15), (1, 16), (2, 16), (3, 16), (3, 15), (4, 15), (5, 15), (5, 16)]


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

# Define characters' images and resize to fit the cell dimensions
# block
block_img = pygame.image.load("resources/sprites/block.png").convert()
block_img = pygame.transform.scale(block_img, (cell_width, cell_height))

# blue_door
blue_door_img = pygame.image.load("resources/sprites/blue_door.png").convert()
blue_door_img = pygame.transform.scale(blue_door_img, (cell_width, cell_height))

# blue_key
blue_key_img = pygame.image.load("resources/sprites/blue_key.png").convert()
blue_key_img = pygame.transform.scale(blue_key_img, (cell_width, cell_height))

# ghost
ghost_img = pygame.image.load("resources/sprites/ghost.png").convert()
ghost_img = pygame.transform.scale(ghost_img, (cell_width, cell_height))

# ghost pink cell
ghost_cell_img = pygame.image.load("resources/sprites/pink_cell.png").convert()
ghost_cell_img = pygame.transform.scale(ghost_cell_img, (cell_width, cell_height))

# green_door
green_door_img = pygame.image.load("resources/sprites/green_door.png").convert()
green_door_img = pygame.transform.scale(green_door_img, (cell_width, cell_height))

# green_key
green_key_img = pygame.image.load("resources/sprites/green_key.png").convert()
green_key_img = pygame.transform.scale(green_key_img, (cell_width, cell_height))

# pacman: Start Point
pacman_img = pygame.image.load("resources/sprites/pacman.png").convert()
pacman_img = pygame.transform.scale(pacman_img, (cell_width, cell_height))

# path
path_img = pygame.image.load("resources/sprites/path.png").convert()
path_img = pygame.transform.scale(path_img, (cell_width, cell_height))

# red_door
red_door_img = pygame.image.load("resources/sprites/red_door.png").convert()
red_door_img = pygame.transform.scale(red_door_img, (cell_width, cell_height))

# red_key
red_key_img = pygame.image.load("resources/sprites/red_key.png").convert()
red_key_img = pygame.transform.scale(red_key_img, (cell_width, cell_height))

# reward: end point
reward_img = pygame.image.load("resources/sprites/reward.png").convert()
reward_img = pygame.transform.scale(reward_img, (cell_width, cell_height))

# yellow_door
yellow_door_img = pygame.image.load("resources/sprites/yellow_door.png").convert()
yellow_door_img = pygame.transform.scale(yellow_door_img, (cell_width, cell_height))

# yellow_key
yellow_key_img = pygame.image.load("resources/sprites/yellow_key.png").convert()
yellow_key_img = pygame.transform.scale(yellow_key_img, (cell_width, cell_height))

# The starting point in the final path
fp_index = 0
current_x = final_path[fp_index][0]
current_y = final_path[fp_index][1]


# Keys and doors
keys_list = [YELLOW_KEY, GREEN_KEY, RED_KEY, BLUE_KEY]
owned_keys = []
doors_keys = {YELLOW_DOOR:YELLOW_KEY, GREEN_DOOR:GREEN_KEY, RED_DOOR:RED_KEY, BLUE_DOOR:BLUE_KEY}
 


# The main loop for which the pygame works
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True               # Done: Exit loop
 
 
    # Draw the grid
    for row in range(len(grid)):
        for column in range(len(grid[0])):    
            position_y = row * cell_height
            position_x = column * cell_width

            # Draw grid elements
            # path
            if grid[row][column] == CELL:
                screen.blit(path_img, (position_x, position_y))

            # block_img
            if grid[row][column] == WALL:
                screen.blit(block_img, (position_x, position_y))
            
            # Pacman: Remove from start point
            if grid[row][column] == grid[final_path[0][0]][final_path[0][1]]: 
                screen.blit(path_img, (position_x, position_y))
            
            # Reward: End point
            if grid[row][column] == END:
                screen.blit(reward_img, (position_x, position_y))
                
            # Doors
            if grid[row][column] == YELLOW_DOOR:
                screen.blit(yellow_door_img, (position_x, position_y))
            if grid[row][column] == GREEN_DOOR:
                screen.blit(green_door_img, (position_x, position_y))
            if grid[row][column] == RED_DOOR:
                screen.blit(red_door_img, (position_x, position_y))
            if grid[row][column] == BLUE_DOOR:
                screen.blit(blue_door_img, (position_x, position_y))

            # Keys
            if grid[row][column] == YELLOW_KEY:
                screen.blit(yellow_key_img, (position_x, position_y))
            if grid[row][column] == GREEN_KEY:
                screen.blit(green_key_img, (position_x, position_y))
            if grid[row][column] == RED_KEY:
                screen.blit(red_key_img, (position_x, position_y))
            if grid[row][column] == BLUE_KEY:
                screen.blit(blue_key_img, (position_x, position_y))

            # Ghosts and their paths
            if grid[row][column].isdigit() and int(grid[row][column]) > 1:
                screen.blit(ghost_img, (position_x, position_y))
            if grid[row][column] == GHOST_RANGE:
                screen.blit(ghost_cell_img, (position_x, position_y))

                
    # Animate Pacman
    if fp_index < len(final_path) - 1:
        fp_index+=1
        current_x = final_path[fp_index][0]
        current_y = final_path[fp_index][1]

        pacman_y = current_x * cell_width
        pacman_x = current_y * cell_height

        grid[row][column] == START
        screen.blit(pacman_img, (pacman_x, pacman_y))
    else:
        # Pause Time in milliseconds
        pygame.time.wait(WAITING_TIME)

        # Exit Game
        done = True

    
    # Track collisions
    # Collision with a key. Add key to the owned keys list
    if grid[current_x][current_y] in keys_list:
        key = grid[current_x][current_y]
        print("Found Key: " + key)
        owned_keys.append(grid[current_x][current_y])
        grid[current_x][current_y] = '0'

    # Collision with door. 
    # Check if relevant key is in owned keys list
    if grid[current_x][current_y] in doors_keys:
        door = grid[current_x][current_y]
        key = doors_keys[door]
        print("Found Door: " , door, "Need Key:" , key)
        if key in owned_keys:
            print("Already have the key. You can pass")
            grid[current_x][current_y] = '0'
            owned_keys.remove(key)

    # Speed: Frames per second
    clock.tick(PACMAN_SPEED)
 
    # Update the screen
    pygame.display.flip()


# Exit Game (KEEP THIS LINE HERE).
pygame.quit()