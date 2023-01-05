import settings
import pygame

class Cell(pygame.sprite.Sprite):

    def __init__(self, i, j):
        super().__init__()
        self.i = i
        self.j = j
        self.x = i * settings.w
        self.y = j * settings.w

        self.image = pygame.Surface((settings.w, settings.w))
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
    
    def update(self):
        self.image.fill('black')
        pygame.draw.rect(self.image, 'white', pygame.Rect(1, 1, settings.w - 2, settings.w - 2))