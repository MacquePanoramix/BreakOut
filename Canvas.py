import pygame
class Canvas():

    def __init__(self):
        self.size = (1200,800)
        self.wallSize = (1200, 700)
        self.wallLoc = (0, 100)
        self.gameSize = (1100, 600)
        self.gameLoc = (50, 150)

        self.color_1 = (0,0,0) #Black
        self.color_2 = (51,136,187) #Blue

    def displayCanvas(self, screen):
        screen.fill(self.color_1)
        pygame.draw.rect(screen, self.color_2, (self.wallLoc[0], self.wallLoc[1], self.wallSize[0], self.wallSize[1]))
        pygame.draw.rect(screen, self.color_1, (self.gameLoc[0], self.gameLoc[1], self.gameSize[0], self.wallSize[1]))

