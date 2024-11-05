import pygame as pg
import random

# Картинки:
#iconarchive.com

# Музыка и звуки
# mixkit.co


# запаковка в exe
# auto-py-to-exe


class Dragon(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.image.load("images/dragon.png")
        self.image = pg.transform.scale(self.image, (80, 80))
        self.image = pg.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        self.rect.topleft = (25, 25)

        self.direction = 'right'

    def update(self):
        # Get a list of all keys pressed down
        keys = pg.key.get_pressed()

        # Move the dragon continuously
        if keys[pg.K_LEFT] and self.rect.left > 0:
            if self.direction == "right":
                self.image = pg.transform.flip(self.image, True, False)
                self.direction = "left"
            self.rect.x -= VELOCITY
        if keys[pg.K_RIGHT] and self.rect.right < WINDOW_WIDTH:
            if self.direction == "left":
                self.image = pg.transform.flip(self.image, True, False)
                self.direction = "right"
            self.rect.x += VELOCITY
        if keys[pg.K_UP] and self.rect.top > 0:
            self.rect.y -= VELOCITY
        if keys[pg.K_DOWN] and self.rect.bottom < WINDOW_HIGHT:
            self.rect.y += VELOCITY

class Coin(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.image.load("images/coin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (WINDOW_WIDTH//2, WINDOW_HIGHT//2)

# Инициализируем pygame
pg.init()

# Иконка
icon = pg.image.load('images/dragon.png')
pg.display.set_icon(icon)

# Создаем игровой дисплей
WINDOW_WIDTH = 600
WINDOW_HIGHT = 300
screen = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HIGHT))
pg.display.set_caption('Hungry Dragon!')


background = pg.image.load("images/background.jpg")
background = pg.transform.scale(background, (WINDOW_WIDTH, WINDOW_HIGHT))


# Устнавливаем FPS
FPS = 60
clock = pg.time.Clock()


# Звуки
sound_1 = pg.mixer.Sound('sounds/sound_1.wav')
# mixkit.com
sound_1.set_volume(0.1)

# Фоновая музыка
pg.mixer.music.load('sounds/music.wav')

# Запуск музыки
pg.mixer.music.set_volume(0.1)
pg.mixer.music.play(-1, 0.0)


# Скорость движения
VELOCITY = 5
# Очки
score = 0

# Шрифт
font = pg.font.Font(None, 40)


# Создаем объекты
dragon = Dragon()
coin = Coin()

# Игровой цикл
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    dragon.update()

    # Проверяем столкновения (коллизии) двух спрайтов
    if dragon.rect.colliderect(coin.rect):
        score += 1
        sound_1.play()
        coin.rect.left = random.randint(0, WINDOW_WIDTH - coin.rect.w)
        coin.rect.top = random.randint(0, WINDOW_HIGHT - coin.rect.h)


    # Фон
    screen.blit(background, (0, 0))  

    # Отрисовка спрайтов
    screen.blit(dragon.image, dragon.rect)
    screen.blit(coin.image, coin.rect)

    # Отрисовка счета
    score_text = font.render(str(score), True, "red")
    screen.blit(score_text, (10, 10))
 
    # Обновляем экран
    pg.display.update()

    clock.tick(FPS)

# Выход из игры
pg.quit()