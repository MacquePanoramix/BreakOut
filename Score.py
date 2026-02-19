import pygame

class Score:
    def __init__(self, x, y):
        self.value = 0
        self.x = x
        self.y = y
        self.color = (255, 255, 255) # whit
        # use sys font
        self.font = pygame.font.SysFont("Arial", 40, bold=True)

    def increase(self):
        # add value when block die
        self.value += 1

    def display(self, screen):
        text_surface = self.font.render(f"Score: {self.value}", True, self.color)
        screen.blit(text_surface, (self.x, self.y))