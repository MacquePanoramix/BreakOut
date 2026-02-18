from Object import Object
import pygame

class Ball(Object):

    def __init__(self, x, y, size_x, size_y):
        Object.__init__(self, x, y, (255,0,0), size_x, size_y)



        self.dx = 2
        self.dy = 2

    def move(self):

        # update pos based on speed
        self.x += self.dx
        self.y += self.dy


    def display(self,screen):
        # This draws the ball
        pygame.draw.ellipse(screen, self.color, [[self.x, self.y], [self.size_x, self.size_y]])


    def bounce_wall(self, wall_left, wall_right, wall_up, wall_down):

        #Bounce loop
        if self.x < wall_left or self.x - self.size_x > wall_right: #HORIZONTAL WALLS
            self.dx *= -1
            self.move()

        if self.y < wall_up or self.y + self.size_y > wall_down: #VERTICAL WALLS
            self.dy *= -1
            self.move()


    def bounce_block(self, block):
        #Collision detection for blocks
        if self.x >= block.x and self.x <= block.x + block.size_x and self.y >= block.y and self.y <= block.y + block.size_y:
            #Bounce horizontally:
            if self.x + self.dx < block.x or self.x - self.dx - self.size_x > block.x + block.size_x:
                self.dx *= -1
                self.move()
                block.hit()
            #Bounce vertically:
            if self.y - self.dy < block.y or self.y + self.dy + self.size_y > block.y + block.size_y:
                self.dy *= -1
                self.move()
                block.hit()


