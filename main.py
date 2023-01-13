import pygame
import sys
import os
bg_image = pygame.image.load(os.path.join('files', 'bg.png'))
player_images = [pygame.image.load(os.path.join('files', 'DinoRun1.png')),
    pygame.image.load(os.path.join('files', 'DinoRun2.png')),
    pygame.image.load(os.path.join('files', 'DinoJump.png'))]

delta_jump = 0.2
jump = 12
bg_pos = bg_x, bg_y = 0, 500
bg_speed = 5



class Dinosour(pygame.sprite.Sprite()):
    def __init__(self):
        super().__init__(self)
        self.condition = 0
        self.image = player_images[self.condition]
        self.x = 50
        self.y = bg_y - self.image.get_height()
        self.image = player_images[self.condition]
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.jump_y = self.y
        self.change_jump = jump

    def update(self):
        if self.condition < 2:
            self.condition = (self.condition + 1) % 2
            self.image = player_images[self.condition]
            self.rect = self.image.get_rect()
            self.rect.x = self.x
            self.rect.y = self.y
        else:
            self.image = player_images[self.condition]
            self.change_jump -= delta_jump
            self.jump_y -= self.change_jump
            self.rect = self.image.get_rect()
            self.rect.x = self.x
            self.rect.y = self.jump_y
            if self.jump_y == self.y:
                self.condition = 0

        def jump(self):
            if self.condition != 2:
                self.condition == 2
                self.jump_y = self.y
                self.change_jump = jump

        def draw(self, screen):
            screen.blit(self.image, (self.rect.x, self.rect.y))




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
    player = Dinosour()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.jump()



        screen.fill((255, 255, 255))
        update(screen)
        player.draw(screen)
        player.update()
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()







if __name__ == '__main__':
    sys.exit(main())