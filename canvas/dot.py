import pygame


class Dot(pygame.Rect):
    def __init__(self, pos, size, color):
        super().__init__(self)
        self.x, self.y = pos
        self.size = size
        self.color = color

    def change_color(self, color):
        self.color = color