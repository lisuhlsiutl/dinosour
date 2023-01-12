import pygame
import sys
import os
bg_image = pygame.image.load(os.path.join('files', 'bg.png'))
bg_pos = bg_x, bg_y = 0, 500
bg_speed = 5

def bg(screen):
    global bg_x, bg_y
    image_w = bg_image.get_width()
    bg_x -= bg_speed
    if bg_x <= -image_w:
        bg_x = image_w
    screen.blit(bg_image, (bg_x, bg_y))
    if bg_x <= 1000 - image_w:
        screen.blit(bg_image, (bg_x + image_w - 1, bg_y))

def update(screen):
    bg(screen)


def main():
    pygame.init()
    pygame.display.set_caption('Динозавр')
    size = width, height = 1000, 600

    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()

    run = True
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        screen.fill((255, 255, 255))
        update(screen)
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()







if __name__ == '__main__':
    sys.exit(main())