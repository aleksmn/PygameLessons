import pygame as pg
import random



class Dragon(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.image.load("images/dragon.png")
        self.image = pg.transform.scale(self.image, (80, 80))

        # self.image = pg.transform.flip(self.image, True, False)

        self.rect = self.image.get_rect()
        self.rect.topleft = (25, 25)

        self.direction = 'right'


    def update(self):
        # Get a list of all keys pressed down
        keys = pg.key.get_pressed()

        if keys[pg.K_LEFT]:
            self.rect.x -= VELOCITY

        if keys[pg.K_RIGHT]:
            self.rect.x += VELOCITY




#Инициализируем pygame
pg.init()

# Создаем игровой дисплей
WINDOW_WIDTH = 600
WINDOW_HIGHT = 300
screen = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HIGHT))
pg.display.set_caption('Hungry Dragon!')

VELOCITY = 5

# Устнавливаем FPS
FPS = 60
clock = pg.time.Clock()

# Объявляем цвета
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)



# Очки
score = 0

# Создаем объекты
dragon = Dragon()




# Игровой цикл
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False


    # Заливка экрана
    screen.fill((BLACK))


    # Отрисовка спрайтов
    screen.blit(dragon.image, dragon.rect)



    # Обновляем экран
    pg.display.update()
    clock.tick(FPS)

# Выход из игры
pg.quit()