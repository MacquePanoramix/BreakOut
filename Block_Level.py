from BlockLayer import BlockLayer
from Block import Block
import random as rd

class Block_Level:

    def __init__(self):


        self.layers = []

        self.layersNumber = 6

        self.blockGap = 100

    def create_layers(self, canvas, block_height, block_width):
        for i in range(self.layersNumber):
            # Add the layers
            self.layers.append(BlockLayer(color = (rd.randint(1,255),rd.randint(1,255),rd.randint(1,255)), startingHealth=6-i, yPos=canvas.gameLoc[1] + self.blockGap + i * block_height, block_count= (canvas.gameSize[0])//block_width ))



    def create_blocks(self, canvas, block_height, block_width):

        #Go over layers to create the blocks
        layer: BlockLayer
        for layer in self.layers:
            layer.create_blocks(canvas, block_height, block_width)


    def update_blocks(self, ball, screen):
        layer: BlockLayer
        for layer in self.layers:
            for block in layer.blocks:
                #FIRST DRAW
                block.display(screen)
                # THEN HANDLE COLLISIONS
                ball.bounce_block(block)
                # Also check if they should be destroyed afterward
                if block.isDead():
                    layer.blocks.remove(block)

