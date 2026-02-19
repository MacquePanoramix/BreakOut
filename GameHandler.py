import pygame
from dask.config import update

from Block_Level import Block_Level

from Canvas import Canvas
from Ball import Ball
from Player import Player
from Score import Score

class GameHandler():

    def __init__(self):

        self.game_running = True

        # text when ball goes offscreen
        self.game_over = False
        pygame.font.init()
        self.font_gameover = pygame.font.SysFont('Arial', 64, bold=True)


    def game_set_up(self, screen, canvas, widthBlocks, heightBlocks):

        # for rebuilding canvas if restart
        self.block_width = widthBlocks
        self.block_height = heightBlocks

        # Initiate Objects
        ball, block_level, player, score = self.create_objects(canvas, widthBlocks, heightBlocks)

        #Run the game loop
        self.game_loop(screen, canvas, ball, block_level, player, score)


    def game_loop(self, screen, canvas, ball, block_level, player, score):

        while self.game_running:

            self.handle_events(player)
            keys = pygame.key.get_pressed()

            # check if restart
            if self.inputs(keys, player, canvas):
                # r pressed, restart
                self.game_over = False
                ball, block_level, player, score = self.create_objects(canvas, self.block_height, self.block_width)

            self.set_up_canvas(screen, canvas)

            # only run class if game not over
            if not self.game_over:
                self.update_blocks(block_level, screen, ball, score)
                self.move_objects(ball, canvas, player)

                # check if ball leaves bottom
                if ball.y > 800:
                    self.game_over = True

            # if game over
            else:
                for layer in block_level.layers:
                    for block in layer.blocks:
                        block.display(screen)

                text_surface = self.font_gameover.render("GAME OVER", True, (255, 0, 0))
                screen.blit(text_surface, (400, 550))

            self.draw_objects(ball, screen, player, score)

            pygame.display.flip()

    def inputs(self, keys, player, canvas):
        #Quit key
        if keys[pygame.K_q]:
            pygame.quit()

        if keys[pygame.K_r]:
            return True

        #Player keys
        player.input(keys, canvas)

        return False

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
        ball = Ball(400,500,25,25)

        #Create player
        player = Player(500,750, 200, 25)

        #Create score
        score = Score(50, 50)

        return ball, block_level, player, score

    def update_blocks(self, block_level, screen, ball, score):

        """All block updates will be handled together due to efficiency reasons of constantly iterating over all the blocks"""
        block_level.update_blocks(ball, screen, score)


    def move_objects(self, ball, canvas, player):

        #Calculate colisions first
        ball.bounce_wall(canvas.gameLoc[0], canvas.gameSize[0], canvas.gameLoc[1], canvas.size[1])
        ball.bounce_player(player)

        ball.move()

    def draw_objects(self, ball, screen, player, score): #except blocks for performance reasons

        #Draw Ball
        ball.display(screen)

        #Draw player
        player.display(screen)

        # draw score
        score.display(screen)



'''
    def game_loop(self, screen, canvas,ball, block_level, player, score):

        while self.game_running:

            self.handle_events(player)
            keys = pygame.key.get_pressed()

            self.inputs(keys, player, canvas)

            #Draw canvas
            self.set_up_canvas(screen, canvas)

            #Handle blocks first
            self.update_blocks(block_level, screen, ball, score)

            #Move Objects
            self.move_objects(ball, canvas, player)

            # Draw objects
            self.draw_objects(ball, screen, player, score)

            pygame.display.flip()  # updates pygame canvas
'''