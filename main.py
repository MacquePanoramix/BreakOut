# This is a sample Python script.

# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pygame
from Canvas import *
from GameHandler import GameHandler




def main():
    # Initiate canvas to be used
    canvas = Canvas()

    #Game settings
    block_height = 25
    block_width = 25

    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    clock  = pygame.time.Clock()

    #Start THE GAME
    game_handler = GameHandler()
    game_handler.game_set_up(screen, canvas, block_width, block_height)


if __name__ == '__main__':
    main()
