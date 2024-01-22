# Number Slider, Nevaeh Copeland, based on a project by Al Sweigart, v0.0

import sys, random, pygame
# sys module provides access to system resources (i.en Operating System Commands)

from pygame.locals import *
# Allows us to call functions from pygame using just the function name instead of module.function()
# Example: We can use draw() ;instead of pygame.draw()

# Constants for game Board
BOARDWIDTH = 4 # COLUMNS
BOARDHEIGHT = 4 # ROWS
TILESIZE = 80 # MEASURED IN PIXELS
WINDOWWIDTH = 640 # MEASURED IN PIXELS
WINDOWHEIGHT = 480 # MEASURED IN PIXELS
FPS = 30
BLANK = None