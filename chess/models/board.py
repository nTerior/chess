from pygame.image import load


class Board:
    def __init__(self, screen):
        self.screen = screen

    def render(self):
        img = load("./assets/board.png")
        self.screen.blit(img, (0, 0))
