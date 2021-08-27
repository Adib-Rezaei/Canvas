import pygame
from settings import WIDTH, HEIGHT

SPEED = 5

def movement_handler(key_pressed, dot):
    if key_pressed[pygame.K_a] and dot.x - SPEED > 0:       # LEFT
        dot.move_ip(-SPEED, 0)
    if key_pressed[pygame.K_d] and dot.x + SPEED < WIDTH:   # RIGHT
        dot.move_ip(SPEED, 0)
    if key_pressed[pygame.K_w] and dot.y - SPEED > 0:       # UP
        dot.move_ip(0, SPEED)
    if key_pressed[pygame.K_s] and dot.y + SPEED < HEIGHT:  # DOWN
        dot.move_ip(0, -SPEED)

def dot_size_handler(key_pressed, dot):
    if key_pressed[pygame.K_EQUALS]:
        dot.inflate_ip(1, 1)

    if key_pressed[pygame.K_MINUS]:
        dot.inflate_ip(-1, -1)

def in_color_palette_handler(mouse_pos, color_palette_dots, dot):
    for colored_dot in color_palette_dots:
        if colored_dot.contains(pygame.Rect(mouse_pos, (1,1))):
            dot.change_color(colored_dot.color)
            # print(colored_dot.color)
            return