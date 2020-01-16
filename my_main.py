import os
import pygame
import sys
import time
from pygame import mixer

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen.fill((255, 255, 255))


# Создаём функции загрузки изображений для различных изображений

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname).convert_alpha()
    return image


def pl_shot_anim_sprite(name):
    fullname = os.path.join('data/pl_attack', name)
    image = pygame.image.load(fullname).convert_alpha()
    return image


def pm1_shot_anim_sprite(name):
    fullname = os.path.join('data/pm1_attack', name)
    image = pygame.image.load(fullname).convert_alpha()
    return image


def pm2_shot_anim_sprite(name):
    fullname = os.path.join('data/pm2_attack', name)
    image = pygame.image.load(fullname).convert_alpha()
    return image


def obst_crashed(name):
    fullname = os.path.join('data/obst_crashed', name)
    image = pygame.image.load(fullname).convert_alpha()
    return image


def player_crashed(name):
    fullname = os.path.join('data/pl_crashed', name)
    image = pygame.image.load(fullname).convert_alpha()
    return image


# Создаём игрока (террориста)
class Player(pygame.sprite.Sprite):

    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.image = player_image
        self.rect = self.image.get_rect().move(pos_x, pos_y)
        self.alive = True

    def update(self, ev):
        if self.alive is True:
            if ev.key == 273:
                if self.rect.y > 750:
                    self.rect = self.rect.move(0, -30)
            elif ev.key == 274:
                if self.rect.y < 900:
                    self.rect = self.rect.move(0, 30)

    def get_rect_pos(self):
        return self.rect.x, self.rect.y

    def died(self):
        self.alive = False
        mixer.music.load("death-sound.mp3")
        mixer.music.play()
        self.image = load_image('pl_died.png')
        self.image = pygame.transform.scale(self.image, (300, 200))
        self.rect = self.image.get_rect().move(self.rect.x, self.rect.y)
        players_bullet.remove(bullet_3)


# Создаём врага (полицейского)
class Enemies(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, img):
        super().__init__(enemies, all_sprites)
        self.image = img
        self.rect = self.image.get_rect().move(pos_x, pos_y)

    def died(self, num):
        if num == 1 and self.image != pm1_died:
            mixer.music.load("death-sound.mp3")
            mixer.music.play()
            self.image = pm1_died
            self.rect = self.image.get_rect().move(1500, 750)
            enemy_bullets.remove(bullet_1)
        elif num == 2 and self.image != pm2_died:
            mixer.music.load("death-sound.mp3")
            mixer.music.play()
            self.image = pm2_died
            self.rect = self.image.get_rect().move(1500, 900)
            enemy_bullets.remove(bullet_2)


# Создаём класс для обновления и анимации пуль врага
class EnemysBullet(pygame.sprite.Sprite):
    image = load_image("bullet.png")
    shot = mixer.Sound('shot_police.wav')

    im1 = pm1_shot_anim_sprite('attack1.png')
    im1 = pygame.transform.scale(im1, (200, 150))
    im2 = pm1_shot_anim_sprite('attack2.png')
    im2 = pygame.transform.scale(im2, (200, 150))
    im3 = pm1_shot_anim_sprite('attack3.png')
    im3 = pygame.transform.scale(im3, (200, 150))
    im4 = pm1_shot_anim_sprite('attack4.png')
    im4 = pygame.transform.scale(im4, (200, 150))
    im5 = pm1_shot_anim_sprite('attack5.png')
    im5 = pygame.transform.scale(im5, (200, 150))
    im6 = pm1_shot_anim_sprite('attack6.png')
    im6 = pygame.transform.scale(im6, (200, 150))

    pm2_im1 = pm2_shot_anim_sprite('attack1.png')
    pm2_im1 = pygame.transform.scale(pm2_im1, (200, 150))
    pm2_im2 = pm2_shot_anim_sprite('attack2.png')
    pm2_im2 = pygame.transform.scale(pm2_im2, (200, 150))
    pm2_im3 = pm2_shot_anim_sprite('attack3.png')
    pm2_im3 = pygame.transform.scale(pm2_im3, (200, 150))
    pm2_im4 = pm2_shot_anim_sprite('attack4.png')
    pm2_im4 = pygame.transform.scale(pm2_im4, (200, 150))
    pm2_im5 = pm2_shot_anim_sprite('attack5.png')
    pm2_im5 = pygame.transform.scale(pm2_im5, (200, 150))
    pm2_im6 = pm2_shot_anim_sprite('attack6.png')
    pm2_im6 = pygame.transform.scale(pm2_im6, (200, 150))

    def __init__(self, x, y):
        super().__init__(enemy_bullets, all_sprites)
        self.image = EnemysBullet.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.count = 0
        self.shot.play()

    def update(self):
        self.count += 1
        if self.count == 2:
            if enemy.image != pm1_died:
                enemy.image = self.im1
            if enemy_2.image != pm2_died:
                enemy_2.image = self.pm2_im1
            enemies.draw(screen)
        elif self.count == 5:
            if enemy.image != pm1_died:
                enemy.image = self.im2
            if enemy_2.image != pm2_died:
                enemy_2.image = self.pm2_im2
            enemies.draw(screen)
        elif self.count == 9:
            if enemy.image != pm1_died:
                enemy.image = self.im3
            if enemy_2.image != pm2_died:
                enemy_2.image = self.pm2_im3
            enemies.draw(screen)
        elif self.count == 12:
            if enemy.image != pm1_died:
                enemy.image = self.im4
            if enemy_2.image != pm2_died:
                enemy_2.image = self.pm2_im4
            enemies.draw(screen)
        elif self.count == 13:
            if enemy.image != pm1_died:
                enemy.image = self.im5
            if enemy_2.image != pm2_died:
                enemy_2.image = self.pm2_im5
            enemies.draw(screen)
        elif self.count == 14:
            if enemy.image != pm1_died:
                enemy.image = self.im6
            if enemy_2.image != pm2_died:
                enemy_2.image = self.pm2_im6
            enemies.draw(screen)
        if self.rect.x <= 150:
            self.shot.play()
            self.rect.x = 1500
            self.count = 0
        screen.blit(self.image, (self.rect.x, self.rect.y))
        if self.count > 12:
            self.rect.x -= 10
        x = player.get_rect_pos()[0]
        y = player.get_rect_pos()[1]
        if pygame.sprite.spritecollideany(self, player_group):
            if self.rect.y - y == 100 and x + 150 == self.rect.x:
                player.died()
            elif self.rect.y - y == 130 and x + 150 == self.rect.x:
                player.died()
            elif self.rect.y - y == 150 and x + 150 == self.rect.x:
                player.died()
            elif self.rect.y - y == 120 and x + 150 == self.rect.x:
                player.died()


# Создаём класс для обновления и анимации пуль игрока
class PlayersBullet(pygame.sprite.Sprite):
    image = load_image("bullet2.png")
    shot = mixer.Sound('shot.wav')
    im1 = pl_shot_anim_sprite('attack1.png')
    im1 = pygame.transform.scale(im1, (300, 200))
    im2 = pl_shot_anim_sprite('attack2.png')
    im2 = pygame.transform.scale(im2, (300, 200))
    im3 = pl_shot_anim_sprite('attack3.png')
    im3 = pygame.transform.scale(im3, (300, 200))
    im4 = pl_shot_anim_sprite('attack4.png')
    im4 = pygame.transform.scale(im4, (300, 200))
    im5 = pl_shot_anim_sprite('attack5.png')
    im5 = pygame.transform.scale(im5, (300, 200))
    im6 = pl_shot_anim_sprite('attack6.png')
    im6 = pygame.transform.scale(im6, (300, 200))

    def __init__(self, x, y):
        super().__init__(players_bullet, all_sprites)
        self.image = PlayersBullet.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.shot.play()
        self.count = 0

    def update(self):
        self.count += 1
        player.x = player.get_rect_pos()[0]
        player.y = player.get_rect_pos()[1]
        x1, y1 = 1500, 800
        x2, y2 = 1500, 950
        if self.count == 2:
            player.image = self.im1
            player_group.draw(screen)
        elif self.count == 4:
            player.image = self.im2
            player_group.draw(screen)
        elif self.count == 6:
            player.image = self.im3
            player_group.draw(screen)
        elif self.count == 8:
            player.image = self.im4
            player_group.draw(screen)
        elif self.count == 9:
            player.image = self.im5
            player_group.draw(screen)
        elif self.count == 10:
            player.image = self.im6
            player_group.draw(screen)
        if self.rect.x >= 1600:
            self.count = 0
            self.shot.play()
            self.rect.x = 300
            self.rect.y = player.y + 130
        screen.blit(self.image, (self.rect.x, self.rect.y))
        if self.count > 8:
            self.rect.x += 10
        if pygame.sprite.spritecollideany(self, enemies):
            if self.rect.x - x1 == 100 and (self.rect.y - y1 == 70 or self.rect.y - y1 == 100):
                enemy.died(1)
                self.rect.x = 300
                self.rect.y = player.y + 130
                self.count = 0
                self.shot.play()
            elif (self.rect.x - x2 == 100
                  and (self.rect.y - y2 == 70 or self.rect.y - y2 == 100)):
                enemy_2.died(2)
                self.rect.x = 300
                self.rect.y = player.y + 130
                self.count = 0
                self.shot.play()


# Класс для создания машины игрока
class Car(pygame.sprite.Sprite):
    image = load_image("car1.png")
    image = pygame.transform.scale(image, (56, 125))
    car_1 = player_crashed('crash1.png')
    car_1 = pygame.transform.scale(car_1, (56, 125))
    car_2 = player_crashed('crash2.png')
    car_2 = pygame.transform.scale(car_2, (56, 125))
    car_3 = player_crashed('crash3.png')
    car_3 = pygame.transform.scale(car_3, (56, 125))
    car_4 = player_crashed('crash4.png')
    car_4 = pygame.transform.scale(car_4, (56, 125))
    car_5 = player_crashed('crash5.png')
    car_5 = pygame.transform.scale(car_5, (56, 125))

    def __init__(self, x, y):
        super().__init__(car_group, all_sprites)
        self.image = Car.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, x, y):
        if pygame.sprite.spritecollideany(self, obst_group) \
                and obst_y - self.rect.y > -100 and 40 > (obst_x - self.rect.x) > -40:
            pygame.mixer.quit()
            pygame.mixer.init()
            obst.crashed()
            mixer.music.load("crash.mp3")
            mixer.music.play()
            time.sleep(3)
            game_over()
        self.rect.x, self.rect.y = x, y


# Класс для создания полицейских машин
class Obstacle(pygame.sprite.Sprite):
    obs_0 = load_image('car.png')
    obs_0 = pygame.transform.scale(obs_0, (56, 125))
    obst1 = obst_crashed('crash1.png')
    obst1 = pygame.transform.scale(obst1, (56, 125))
    obst2 = obst_crashed('crash2.png')
    obst2 = pygame.transform.scale(obst2, (56, 125))
    obst3 = obst_crashed('crash3.png')
    obst3 = pygame.transform.scale(obst3, (56, 125))
    obst4 = obst_crashed('crash4.png')
    obst4 = pygame.transform.scale(obst4, (56, 125))
    obst5 = obst_crashed('crash5.png')
    obst5 = pygame.transform.scale(obst5, (56, 125))

    def __init__(self, x, y):
        super().__init__(obst_group, all_sprites)
        self.image = self.obs_0
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, x, y):
        self.rect.x, self.rect.y = x, y

    def crashed(self):
        self.image = self.obst1
        car.image = car.car_1
        obst_group.draw(race_screen)
        car_group.draw(race_screen)
        pygame.display.flip()
        for i in range(1000000):
            i += 1
        self.image = self.obst2
        car.image = car.car_2
        obst_group.draw(race_screen)
        car_group.draw(race_screen)
        pygame.display.flip()
        for i in range(1000000):
            i += 1
        self.image = self.obst3
        car.image = car.car_3
        obst_group.draw(race_screen)
        car_group.draw(race_screen)
        pygame.display.flip()
        for i in range(1000000):
            i += 1
        self.image = self.obst4
        car.image = car.car_4
        obst_group.draw(race_screen)
        car_group.draw(race_screen)
        pygame.display.flip()
        for i in range(1000000):
            i += 1
        self.image = self.obst5
        car.image = car.car_5
        car_group.draw(race_screen)
        obst_group.draw(race_screen)
        pygame.display.flip()


# Выход из программы
def terminate():
    pygame.quit()
    sys.exit()


# Стартовый экран
def start_screen():
    intro_text = ["             Вы играете за террориста, который ограбил банк.",
                  "             Отряды полиции ещё не прибыли, поэтому",
                  "надо расправиться всего с двумя полицейскими.",
                  "             Если вам удастся их нейтрализовать, то",
                  "в качестве следующего испытания",
                  "предстоит уехать от полицейских машин,",
                  "             Кнопки управления:",
                  "             ESC - Выход, стрелки вверх, вниз (для 1 уровня), ",
                  "             и влево, вправо (для 2 уровня)",
                  "             Для начала игры нажмите",
                  "на любую клавишу."]
    font = pygame.font.Font(None, 60)
    text_coord = 300
    screen.fill(pygame.color.Color('black'))
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 300
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    terminate()
                return  # начинаем игру
        pygame.display.flip()


# Победа в перестрелке
def win():
    global level_2
    intro_text = ["Враги нейтрализованы.",
                  "Для продолжения",
                  "нажмите на любую клавишу"]
    screen.fill(pygame.Color('white'))
    font = pygame.font.Font(None, 60)
    text_coord = 500
    win_background = load_image('win_background.jpg')
    screen.blit(win_background, (0, 0))
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('yellow'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 750
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    terminate()
                level_2 = True
                return  # start level 2
        pygame.display.flip()


# Победа в игре
def win_2():
    intro_text = ["Вы успешно сбежали от погони",
                  "и ограбили банк!"]
    screen.fill(pygame.Color('white'))
    font = pygame.font.Font(None, 25)
    text_coord = 80
    win_background = load_image('win2.jpg')
    screen.blit(win_background, (0, 0))
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('yellow'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 135
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    terminate()
        pygame.display.flip()


# Поражение
def game_over():
    intro_text = ["К сожалению, вы проиграли."]
    screen.fill(pygame.Color('black'))
    font = pygame.font.Font(None, 50)
    text_coord = 80
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('yellow'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 100
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    terminate()
        pygame.display.flip()


# Загрузка фона для погони
def bcgr():
    strip = load_image("strip.jpg")
    yellow_strip = load_image("yellow strip.jpg")
    backgroundpic = load_image("download12.jpg")
    race_screen.fill(pygame.color.Color('gray'))
    race_screen.blit(backgroundpic, (0, 0))
    race_screen.blit(backgroundpic, (0, 200))
    race_screen.blit(backgroundpic, (0, 400))
    race_screen.blit(backgroundpic, (700, 0))
    race_screen.blit(backgroundpic, (700, 200))
    race_screen.blit(backgroundpic, (700, 400))
    race_screen.blit(yellow_strip, (400, 100))
    race_screen.blit(yellow_strip, (400, 200))
    race_screen.blit(yellow_strip, (400, 300))
    race_screen.blit(yellow_strip, (400, 400))
    race_screen.blit(yellow_strip, (400, 100))
    race_screen.blit(yellow_strip, (400, 500))
    race_screen.blit(yellow_strip, (400, 0))
    race_screen.blit(yellow_strip, (400, 600))
    race_screen.blit(strip, (120, 200))
    race_screen.blit(strip, (120, 0))
    race_screen.blit(strip, (120, 100))
    race_screen.blit(strip, (680, 100))
    race_screen.blit(strip, (680, 0))
    race_screen.blit(strip, (680, 200))


start_screen()

# Перестрелка

player_image = load_image('player.png')
player_image = pygame.transform.scale(player_image, (300, 200))

policeman_1 = load_image('policeman_1.png')
policeman_1 = pygame.transform.scale(policeman_1, (200, 150))

policeman_2 = load_image('policeman_2.png')
policeman_2 = pygame.transform.scale(policeman_2, (200, 150))

pm1_died = load_image('pm1_died.png')
pm1_died = pygame.transform.scale(pm1_died, (300, 200))

pm2_died = load_image('pm2_died.png')
pm2_died = pygame.transform.scale(pm2_died, (300, 200))

all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
player_group = pygame.sprite.Group()
enemy_bullets = pygame.sprite.Group()
players_bullet = pygame.sprite.Group()

player = Player(20, 800)
enemy = Enemies(1500, 800, policeman_1)
enemy_2 = Enemies(1500, 950, policeman_2)
bullet_1 = EnemysBullet(1500, 900)
bullet_2 = EnemysBullet(1500, 1040)
bullet_3 = PlayersBullet(300, 930)

FPS = 30
clock = pygame.time.Clock()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen.fill((255, 255, 255))
level_2 = False
background = load_image('background.png')
screen.blit(background, (0, 0))
while True:
    if level_2 is True:
        break
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                terminate()
            player_group.update(event)
    enemy_bullets.update()
    players_bullet.update()
    players_bullet.draw(screen)
    enemy_bullets.draw(screen)
    enemies.draw(screen)
    player_group.draw(screen)
    pygame.display.flip()
    screen.blit(background, (0, 0))
    clock.tick(FPS)
    if len(enemy_bullets) == 0:
        time.sleep(2)
        win()
    if len(players_bullet) == 0:
        time.sleep(2)
        game_over()

# Погоня

race_screen = pygame.display.set_mode((800, 600))
race_screen.fill((255, 255, 255))

car_group = pygame.sprite.Group()
obst_group = pygame.sprite.Group()

x = (800 * 0.45)
y = (600 * 0.8)
FPS = 25
bcgr()
car = Car(x, y)
obst = Obstacle(x, 0)
x_change = 0
obst_y = 0
obst_x = x
obs_width = 56
obs_height = 125
obst_counter = 0
mixer.music.load("sirena.mp3")
mixer.music.play()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                terminate()
            if event.key == pygame.K_LEFT:
                x_change = -5
            if event.key == pygame.K_RIGHT:
                x_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
    if obst_y >= 800:
        obst_x = x
        obst_y = 0
        obst_group.update(obst_x, obst_y)
        obst_counter += 1
    if obst_counter == 8:
        pygame.mixer.quit()
        win_2()
        break
    obst_y += 15
    x += x_change
    if 625 >= x >= 125:
        car_group.update(x, y)
    else:
        car_group.update(x, y)
        x -= x_change
    obst_group.update(obst_x, obst_y)
    obst_group.draw(race_screen)
    car_group.draw(race_screen)
    pygame.display.flip()
    bcgr()
    clock.tick(FPS)
