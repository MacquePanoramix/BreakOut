from Block import Block

class BlockLayer:


    def __init__(self, color, startingHealth, yPos, block_count):

        self.color = color
        self.startingHealth = startingHealth
        self.y = yPos
        self.block_count = block_count

        self.blocks = []


    def create_blocks(self, canvas, block_length, block_height):

        for block_number in range(self.block_count):
            self.blocks.append(Block(canvas.gameLoc[0] + block_number* block_length, self.y, self.color,block_length, block_height, self.startingHealth))




