import pygame

from Object import Object

class Player(Object):

    def __init__(self, x, y, size_x, size_y):
        Object.__init__(self, x, y, (0,0,255), size_x, size_y)

        self.speed = 0.5

    def input(self, key, canvas):
        #Arrows
        if key[pygame.K_LEFT]:
            if self.x > canvas.gameLoc[0]: #BORDER CONTROL
                self.x -= self.speed
        if key[pygame.K_RIGHT]:
            if self.x < canvas.gameLoc[0]+canvas.gameSize[0] - self.size_x: #BORDER CONTROL
                self.x += self.speed

        #WASD
        if key[pygame.K_a]:
            if self.x > canvas.gameLoc[0]:  # BORDER CONTROL
                self.x -= self.speed
        if key[pygame.K_d]:
            if self.x < canvas.gameLoc[0] + canvas.gameSize[0] - self.size_x:  # BORDER CONTROL
                self.x += self.speed

    def display(self, screen):
        # This draws the player bar
        pygame.draw.rect(screen, self.color, [[self.x, self.y], [self.size_x, self.size_y]])