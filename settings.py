import pygame

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
BLUE = (50, 153, 213)

# Snake block size
BLOCK_SIZE = 20

# Frames per second controller
SPEED = 15

# Initialize fonts
pygame.font.init()
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
