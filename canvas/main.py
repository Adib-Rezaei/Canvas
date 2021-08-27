import pygame
pygame.init()

from dot import Dot
from colors import *
from terminate import terminate
from settings import COLORED_DOT_SIZE, ERASER_SIZE, PRIMARY_DOT_SIZE, WIDTH, HEIGHT, FPS
from action_handlers import dot_size_handler, in_color_palette_handler, movement_handler
from pygame.constants import MOUSEBUTTONDOWN
from custom_events import RESTART_EVENT, restart
from draw import draw_color_palette, draw_screen


def init():
    global screen
    screen = pygame.display.set_mode(size=(WIDTH, HEIGHT))
    pygame.display.set_caption("Canvas")


def main():
    
    init()

    dot = Dot((0, HEIGHT), PRIMARY_DOT_SIZE, WHITE)
    eraser = Dot((0, HEIGHT), ERASER_SIZE, BLACK)
    
    color_palette_dots = [
        Dot((10, 10), COLORED_DOT_SIZE, WHITE),
        Dot((40, 10), COLORED_DOT_SIZE, BLUE), 
        Dot((10, 40), COLORED_DOT_SIZE, RED), 
        Dot((40, 40), COLORED_DOT_SIZE, GREEN),
    ]

    pygame.Surface.fill(screen, BLACK)
    clock = pygame.time.Clock()

    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()

            if event.type == RESTART_EVENT:
                pygame.Surface.fill(screen, BLACK)
                dot.x, dot.y = 0, HEIGHT
                break

            if pygame.mouse.get_pressed()[0]:
                mouse_pos = pygame.mouse.get_pos()
                in_color_palette_handler(mouse_pos, color_palette_dots, dot)
                point = [coordinate - dot.w//2 for coordinate in mouse_pos]
                dot.update(point, dot.size)

            if pygame.mouse.get_pressed()[2]:
                mouse_pos = pygame.mouse.get_pos()
                point = [coordinate - eraser.w//2 for coordinate in mouse_pos]
                eraser.update(point, eraser.size)
                

        key_pressed = pygame.key.get_pressed()
        movement_handler(key_pressed, dot)
        dot_size_handler(key_pressed, dot)
        restart(key_pressed)
        draw_screen(screen, dot, eraser)
        draw_color_palette(screen, color_palette_dots)
        pygame.display.update()

    main()


if __name__ == '__main__':
    main()