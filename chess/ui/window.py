import pygame

WINDOW_SIZE = 600
TILE_SIZE = WINDOW_SIZE / 8


def on_event(event):
    if event.type == pygame.QUIT:
        exit(0)


def show_window():
    pygame.init()
    size = WINDOW_SIZE, WINDOW_SIZE
    screen = pygame.display.set_mode(size=size)
    pygame.display.set_caption("Chess")
    return screen
