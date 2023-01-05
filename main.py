import pygame
from pygame.locals import *    
import settings
from cell import Cell


def main():
    settings.init()

    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption('snake')

    # Initialise background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill('red')

    # Initialise clock
    clock = pygame.time.Clock()

    # Initialise grid
    cells = pygame.sprite.Group()

    for i in range(settings.cols):
        for j in range(settings.rows):
            settings.grid[i][j] = Cell(i, j)
            cells.add(settings.grid[i][j])

    while True:
        clock.tick(60);

        for event in pygame.event.get():
            if event.type == QUIT:
                return

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return

        screen.blit(background, (0, 0))

        cells.update()
        cells.draw(screen)

        pygame.display.update()

if __name__ == '__main__':
    main()

pygame.quit()
quit()
