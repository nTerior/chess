import pygame

from models.board import Board
from shell.shell import Shell
from ui.window import show_window, on_event

shell = Shell("../chess_shell")

screen = show_window()
board = Board(screen)

while 1:
    for event in pygame.event.get():
        on_event(event)

    screen.fill((255, 255, 255))
    board.render()
    pygame.display.flip()
