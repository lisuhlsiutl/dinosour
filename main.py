import pygame
import sys

def main():
    pygame.init()
    pygame.display.set_caption('Динозавр')
    size = width, height = 1000, 600

    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    while pygame.event.wait().type != pygame.QUIT:
        screen.fill((255, 255, 255))

        pygame.display.flip()
        clock.tick(50)

    pygame.quit()





if __name__ == '__main__':
    sys.exit(main())