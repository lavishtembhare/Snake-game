import pygame
from settings import font_style, score_font, WIDTH, HEIGHT

def message(screen, msg, color):
    """Display a message in the center of the screen."""
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [WIDTH / 6, HEIGHT / 3])

def your_score(screen, score):
    """Display the current score on the screen."""
    value = score_font.render("Your Score: " + str(score), True, (50, 153, 213))
    screen.blit(value, [0, 0])
