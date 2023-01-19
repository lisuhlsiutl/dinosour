import pygame
import sys
import os
from random import randint

#загружаем картинки
bg_image = pygame.image.load(os.path.join('files', 'bg.png'))
player_images = [pygame.image.load(os.path.join('files', 'DinoRun1.png')),
    pygame.image.load(os.path.join('files', 'DinoRun2.png')),
    pygame.image.load(os.path.join('files', 'DinoJump.png'))]
cactus_images = [pygame.image.load(os.path.join('files', 'cactus1.png')),
    pygame.image.load(os.path.join('files', 'cactus2.png')),
    pygame.image.load(os.path.join('files', 'cactus3.png'))]
pygame.init()
sound_jump = pygame.mixer.Sound(os.path.join('files', 'jump.wav'))
sound_finish = pygame.mixer.Sound(os.path.join('files', 'finish.wav'))

#основные константы для позиций
size = width, height = 1000, 600

bg_pos = bg_x, bg_y = 0, 500
speed = 8

jump_delta_y = 1
jump_start_y = 20



class Dinosour(pygame.sprite.Sprite):
    def __init__(self):
        #super().__init__(self)
        pygame.sprite.Sprite.__init__(self)
        self.condition = 0 # 0 и 1 - бег, 2 - прыжок
        self.step = 0
        self.image = player_images[self.condition]
        self.x = 50
        self.y = bg_y - self.image.get_height()
        self.image = player_images[self.condition]
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.jump_y = self.y
        self.change_jump = jump_start_y

    def update(self):
        self.step += 1
        if self.condition < 2: # run
            if self.step > 10:
                self.condition = (self.condition + 1) % 2
                self.step = 0
            self.image = player_images[self.condition]
            self.rect = self.image.get_rect()
            self.rect.x = self.x
            self.rect.y = self.y
        else:
            self.image = player_images[self.condition] # jump
            self.change_jump -= jump_delta_y
            self.jump_y -= self.change_jump
            self.rect = self.image.get_rect()
            self.rect.x = self.x
            self.rect.y = self.jump_y
            if self.jump_y > self.y:
                self.condition = 0

    def jump(self):
        if self.condition != 2:
            self.condition = 2
            sound_jump.play()
            self.jump_y = self.y
            self.change_jump = jump_start_y

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))


class Cactus(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = cactus_images[randint(0,len(cactus_images)-1)]
        self.x = width
        self.y = self.y = bg_y - self.image.get_height()
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.x -= speed
        if self.x <= - self.image.get_width():
            return True
        return False

    def draw(self,screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))



def bg(screen):
    global bg_x, bg_y
    image_w = bg_image.get_width()
    bg_x -= speed
    if bg_x <= -image_w:
        bg_x = image_w
    screen.blit(bg_image, (bg_x, bg_y))
    if bg_x <= width - image_w:
        screen.blit(bg_image, (bg_x + image_w , bg_y))
    if bg_x >= 0:
        screen.blit(bg_image, (bg_x - image_w , bg_y))


def finish_game(screen, score):
    run = True
    sound_finish.play()
    screen.fill((255, 255, 255))
    font = pygame.font.SysFont('arial', 30)
    text = font.render('счёт за игру: ' + str(score // 10), True, (0, 0, 0))
    score_rect = text.get_rect()
    score_rect.center = (width // 2, height // 2)
    screen.blit(text, score_rect)
    pygame.display.flip()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False



def main():
    pygame.display.set_caption('Динозавр')


    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()

    run = True
    player = Dinosour()
    game_score = 0
    cactus_time = 20
    cactus_list = []

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            # обработка нажатий клавиш
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE: # пробел
                    player.jump()

        screen.fill((255, 255, 255))



        # обновляем и отрисовываем все объекты
        bg(screen)
        player.draw(screen)
        player.update()

        # отображение счета на экране во время игры
        font = pygame.font.SysFont('arial', 30)
        text = font.render('счёт за игру: ' + str(game_score // 10), True, (0, 0, 0))
        score_rect = text.get_rect()
        score_rect.center = (width - 150, 30)
        screen.blit(text, score_rect)

        if game_score == cactus_time:
            cactus_time += randint(50,150)
            cactus_list.append(Cactus())
        for c in cactus_list:
            c.draw(screen)
            if player.rect.colliderect(c.rect):
                finish_game(screen, game_score)
                run = False
                break
            kill_cactus = c.update()
            if kill_cactus: cactus_list.remove(c)


        pygame.display.flip()
        game_score += 1
        clock.tick(30)


    pygame.quit()







if __name__ == '__main__':
    sys.exit(main())