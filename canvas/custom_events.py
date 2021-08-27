import pygame

RESTART_EVENT = pygame.USEREVENT + 1
def restart(key_pressed):
    if key_pressed[pygame.K_r]:
        pygame.event.post(pygame.event.Event(RESTART_EVENT))