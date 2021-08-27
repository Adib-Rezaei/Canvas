import pygame
from colors import BLACK, BLUE, GREEN, RED, WHITE, YELLOW
from settings import FONT

def draw_screen(screen, color_palette_dots, primary_dot, eraser):
    # pygame.draw.rect(screen, BLACK, BACKGROUND)

    pygame.draw.rect(screen, primary_dot.color, primary_dot)
    color_palette_board = pygame.Rect(0, 0, 70, 70)
    color_palette_shadow_board = pygame.Rect(0, 0, 75, 75)
    
    pygame.draw.rect(screen, eraser.color, eraser)
    pygame.draw.rect(screen, WHITE, color_palette_shadow_board)
    pygame.draw.rect(screen, BLACK, color_palette_board)
    for colored_dot in color_palette_dots:
        pygame.draw.rect(screen, colored_dot.color, colored_dot)

    pygame.display.update()