import pygame

from Object import Object

class Block(Object):

    def __init__(self, x, y, color, size_x, size_y, starting_health):
        Object.__init__(self, x, y, color, size_x, size_y)

        self.health = starting_health

        self.starting_health = starting_health #We'll use this for damage color

        self.damage_color_coefficient = 7



    def display(self, screen):
        pygame.draw.rect(screen, self.color, [[self.x, self.y], [self.size_x, self.size_y]])


    def hit(self):
        self.health -= 1

        #make the color darker
        self.color = (self.color[0]/(1+(1/self.starting_health)), self.color[1]/(1+(1/self.starting_health)), self.color[2]/(1+(1/self.starting_health)))


    def isDead(self):

        return self.health <= 0






