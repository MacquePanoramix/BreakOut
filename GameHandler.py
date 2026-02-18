import pygame
from dask.config import update

from Block_Level import Block_Level

from Canvas import Canvas
from Ball import Ball
from Player import Player

class GameHandler():

    def __init__(self):

        self.game_running = True


    def game_set_up(self, screen, canvas, widthBlocks, heightBlocks):
        # Initiate Objects
        ball, block_level, player = self.create_objects(canvas, widthBlocks, heightBlocks)

        #Run the game loop
        self.game_loop(screen, canvas, ball, block_level, player)

    def game_loop(self, screen, canvas,ball, block_level, player):

        while self.game_running:

            self.handle_events(player)
            keys = pygame.key.get_pressed()

            self.inputs(keys, player, canvas)

            #Draw canvas
            self.set_up_canvas(screen, canvas)

            #Handle blocks first
            self.update_blocks(block_level, screen, ball)

            #Move Objects
            self.move_objects(ball, canvas, player)

            # Draw objects
            self.draw_objects(ball, screen, player)

            pygame.display.flip()  # updates pygame canvas


    def inputs(self, keys, player, canvas):
        #Quit key
        if keys[pygame.K_q]:
            pygame.QUIT

        #Player keys
        player.input(keys, canvas)

    def handle_events(self, player):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If the screen is closed, quit the program
                self.game_running = False
                pygame.quit()


    def set_up_canvas(self, screen, canvas):
        canvas.displayCanvas(screen)  # canvas


    def create_objects(self, canvas, block_height, block_width):

        #Create blocks
        block_level = Block_Level()
        block_level.create_layers(canvas, block_height, block_width)
        block_level.create_blocks(canvas, block_height, block_width)

        #Create ball
        ball = Ball(500,500,25,25)

        #Create player
        player = Player(500,750, 200, 25)

        return ball, block_level, player

    def update_blocks(self, block_level, screen, ball):

        """All block updates will be handled together due to efficiency reasons of constantly iterating over all the blocks"""
        block_level.update_blocks(ball, screen)


    def move_objects(self, ball, canvas, player):

        #Calculate colisions first
        ball.bounce_wall(canvas.gameLoc[0], canvas.gameSize[0], canvas.gameLoc[1], canvas.size[1])
        ball.bounce_player(player)

        ball.move()

    def draw_objects(self, ball, screen, player): #except blocks for performance reasons

        #Draw Ball
        ball.display(screen)

        #Draw player
        player.display(screen)

