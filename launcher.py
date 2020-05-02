
# coding: utf-8

# ### Python Week 3-day challenge
# #### Group 23
# #### Students: Anh Tu NGUYEN -  Joseph MERHEB - Sita SHRESTHA

# In[1]:


# Cell Dimensions
CELL_WIDTH = 36
CELL_HEIGHT = 36

# Waiting time at the end
WAITING_TIME = 3000

# Pacman speed. Fames/second
PACMAN_SPEED = 5

# Constants
CELL = '0'
WALL = '1'
START = 's'
END = 'e'
YELLOW_KEY = 'a'
YELLOW_DOOR = 'b'
GREEN_DOOR = 'c'
GREEN_KEY = 'd'
RED_KEY = 'f'
RED_DOOR = 'g'
BLUE_KEY = 'h'
BLUE_DOOR = 'i'
GHOST_RANGE = 'x'


# In[2]:


import pygame
import sys
import copy
from reader import *
from runner import *

# Main Class to run the game in UI mode 
class Launcher:
    def __init__(self, input_file):
        # Initiate instance of Reader class
        reader = Reader()
        maze_to_display = reader.read_file(input_file)
        maze_to_run = copy.deepcopy(maze_to_display)
        # Initiate instance of Runner class
        runner = Runner(maze_to_run)
        final_tuple = runner.run()

        # Run UI
        self.display_ui(maze_to_display, final_tuple)



    # Display the UI following the given maze and path
    def display_ui(self, maze, final_tuple):
        # The starting point in the final path
        ft_index = 0
        current_x = final_tuple[ft_index][0]
        current_y = final_tuple[ft_index][1]

        # Initialize pygame
        pygame.init()
        
        # Set the height and width of the screen
        maze_width = CELL_WIDTH  * len(maze[0])
        maze_height = CELL_HEIGHT * len(maze)
        grid_size = [maze_width, maze_height]
        screen = pygame.display.set_mode(grid_size)

        # Set title of screen
        pygame.display.set_caption("Epita Maze v0.0.1")
        
        # Loop until the user clicks the close button.
        done = False
        
        # Used to manage how fast the screen updates
        clock = pygame.time.Clock()

        # Define grid elements and resize to fit the cell dimensions
        # Wall
        BLOCK_IMG = pygame.image.load("resources/sprites/block.png").convert()
        BLOCK_IMG = pygame.transform.scale(BLOCK_IMG, (CELL_WIDTH, CELL_HEIGHT))

        # Blue door
        BLUE_DOOR_IMG = pygame.image.load("resources/sprites/blue_door.png").convert()
        BLUE_DOOR_IMG = pygame.transform.scale(BLUE_DOOR_IMG, (CELL_WIDTH, CELL_HEIGHT))

        # Blue key
        BLUE_KEY_IMG = pygame.image.load("resources/sprites/blue_key.png").convert()
        BLUE_KEY_IMG = pygame.transform.scale(BLUE_KEY_IMG, (CELL_WIDTH, CELL_HEIGHT))

        # Ghost
        GHOST_IMG = pygame.image.load("resources/sprites/ghost.png").convert()
        GHOST_IMG = pygame.transform.scale(GHOST_IMG, (CELL_WIDTH, CELL_HEIGHT))

        # Ghost pink cell
        GHOST_CELL_IMG = pygame.image.load("resources/sprites/pink_cell.png").convert()
        GHOST_CELL_IMG = pygame.transform.scale(GHOST_CELL_IMG, (CELL_WIDTH, CELL_HEIGHT))

        # Green door
        GREEN_DOOR_IMG = pygame.image.load("resources/sprites/green_door.png").convert()
        GREEN_DOOR_IMG = pygame.transform.scale(GREEN_DOOR_IMG, (CELL_WIDTH, CELL_HEIGHT))

        # Green key
        GREEN_KEY_IMG = pygame.image.load("resources/sprites/green_key.png").convert()
        GREEN_KEY_IMG = pygame.transform.scale(GREEN_KEY_IMG, (CELL_WIDTH, CELL_HEIGHT))

        # Pacman: Start Point
        PACMAN_IMG = pygame.image.load("resources/sprites/pacman.png").convert()
        PACMAN_IMG = pygame.transform.scale(PACMAN_IMG, (CELL_WIDTH, CELL_HEIGHT))

        # Path
        PATH_IMG = pygame.image.load("resources/sprites/path.png").convert()
        PATH_IMG = pygame.transform.scale(PATH_IMG, (CELL_WIDTH, CELL_HEIGHT))

        # Red door
        RED_DOOR_IMG = pygame.image.load("resources/sprites/red_door.png").convert()
        RED_DOOR_IMG = pygame.transform.scale(RED_DOOR_IMG, (CELL_WIDTH, CELL_HEIGHT))

        # Red key
        RED_KEY_IMG = pygame.image.load("resources/sprites/red_key.png").convert()
        RED_KEY_IMG = pygame.transform.scale(RED_KEY_IMG, (CELL_WIDTH, CELL_HEIGHT))

        # Reward: end point
        REWARD_IMG = pygame.image.load("resources/sprites/reward.png").convert()
        REWARD_IMG = pygame.transform.scale(REWARD_IMG, (CELL_WIDTH, CELL_HEIGHT))

        # Yellow door
        YELLOW_DOOR_IMG = pygame.image.load("resources/sprites/yellow_door.png").convert()
        YELLOW_DOOR_IMG = pygame.transform.scale(YELLOW_DOOR_IMG, (CELL_WIDTH, CELL_HEIGHT))

        # Yellow key
        YELLOW_KEY_IMG = pygame.image.load("resources/sprites/yellow_key.png").convert()
        YELLOW_KEY_IMG = pygame.transform.scale(YELLOW_KEY_IMG, (CELL_WIDTH, CELL_HEIGHT))

        # Keys and doors
        keys_list = [YELLOW_KEY, GREEN_KEY, RED_KEY, BLUE_KEY]
        owned_keys = []
        doors_keys = {YELLOW_DOOR:YELLOW_KEY, GREEN_DOOR:GREEN_KEY, RED_DOOR:RED_KEY, BLUE_DOOR:BLUE_KEY}
        

        # The main loop for which the pygame works
        while not done:
            for event in pygame.event.get():  # User did something
                if event.type == pygame.QUIT: # If user clicked close
                    done = True               # Done: Exit loop
        
        
            # Draw the maze
            for row in range(len(maze)):
                for column in range(len(maze[0])):    
                    position_y = row * CELL_HEIGHT
                    position_x = column * CELL_WIDTH

                    # Draw maze elements
                    # Path
                    if maze[row][column] == CELL:
                        screen.blit(PATH_IMG, (position_x, position_y))
                        
                    # Wall
                    if maze[row][column] == WALL:
                        screen.blit(BLOCK_IMG, (position_x, position_y))
                    
                    # Pacman: Remove from start point
                    if maze[row][column] == maze[final_tuple[0][0]][final_tuple[0][1]]:
                        screen.blit(PATH_IMG, (position_x, position_y))
                    
                    # Reward: End point
                    if maze[row][column] == END:
                        screen.blit(REWARD_IMG, (position_x, position_y))
                        
                    # Doors
                    if maze[row][column] == YELLOW_DOOR:
                        screen.blit(YELLOW_DOOR_IMG, (position_x, position_y))
                    if maze[row][column] == GREEN_DOOR:
                        screen.blit(GREEN_DOOR_IMG, (position_x, position_y))
                    if maze[row][column] == RED_DOOR:
                        screen.blit(RED_DOOR_IMG, (position_x, position_y))
                    if maze[row][column] == BLUE_DOOR:
                        screen.blit(BLUE_DOOR_IMG, (position_x, position_y))

                    # Keys
                    if maze[row][column] == YELLOW_KEY:
                        screen.blit(YELLOW_KEY_IMG, (position_x, position_y))
                    if maze[row][column] == GREEN_KEY:
                        screen.blit(GREEN_KEY_IMG, (position_x, position_y))
                    if maze[row][column] == RED_KEY:
                        screen.blit(RED_KEY_IMG, (position_x, position_y))
                    if maze[row][column] == BLUE_KEY:
                        screen.blit(BLUE_KEY_IMG, (position_x, position_y))

                    # Ghosts and their paths
                    if maze[row][column].isdigit() and int(maze[row][column]) > 1:
                        screen.blit(GHOST_IMG, (position_x, position_y))
                    if maze[row][column] == GHOST_RANGE:
                        screen.blit(GHOST_CELL_IMG, (position_x, position_y))

                        
            # Animate Pacman
            if ft_index < len(final_tuple) - 1:
                ft_index+=1
                current_x = final_tuple[ft_index][0]
                current_y = final_tuple[ft_index][1]
                pacman_y = current_x * CELL_WIDTH
                pacman_x = current_y * CELL_HEIGHT
                maze[row][column] == START
                screen.blit(PACMAN_IMG, (pacman_x, pacman_y))
            else:
                # Pause Time in milliseconds
                pygame.time.wait(WAITING_TIME)

                # Exit Game
                done = True

            
            # Track collisions
            # Collision with a key. Add key to the owned keys list
            if maze[current_x][current_y] in keys_list:
                key = maze[current_x][current_y]
                print("Found Key: " + key)
                owned_keys.append(maze[current_x][current_y])
                maze[current_x][current_y] = '0'


            # Collision with door. Check if relevant key is in owned keys list
            if maze[current_x][current_y] in doors_keys:
                door = maze[current_x][current_y]
                key = doors_keys[door]
                print("Found Door: " , door, "Need Key:" , key)
                if key in owned_keys:
                    print("Already have the key. You can pass")
                    maze[current_x][current_y] = '0'
                    owned_keys.remove(key)

            # Speed: Frames per second
            clock.tick(PACMAN_SPEED)
        
            # Update the screen
            pygame.display.flip()


        # Exit Game (KEEP THIS LINE HERE).
        pygame.quit()


# In[3]:


def main():
    # Put file path while running
    filepath = ""
    if len (sys.argv) != 2:
        print('Please put the file name as argument. Ex: python search.py Maze1.txt')
        sys.exit (1)
    else:
        filepath = sys.argv[1]
    
    launcher = Launcher(filepath)
    
if __name__ == "__main__":
    main()

