import pygame as pg
import random



class Dragon(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.image.load("images/dragon.png")
        # изменяем размер
        self.image = pg.transform.scale(self.image, (80, 80))
        # получим прямоугольник от кортинки
        self.rect = self.image.get_rect()
        # указываем расположение
        self.rect.topleft = (25, 25)

        self.direction = 'right'

    def update(self):
        # Получаем список нажатых клавиш
        keys = pg.key.get_pressed()

        if keys[pg.K_RIGHT] and self.rect.right < WINDOW_WIDTH:
            self.rect.x += 5

        if keys[pg.K_LEFT] and self.rect.left > 0:
            self.rect.x -= 5






class Coin(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.image.load("images/coin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (WINDOW_WIDTH//2, WINDOW_HIGHT//2)



#Инициализируем pygame
pg.init()

# Создаем игровой дисплей
WINDOW_WIDTH = 600
WINDOW_HIGHT = 600
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
coin = Coin()

# Игровой цикл
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False


    # Заливка экрана
    screen.fill(BLACK)

    dragon.update()

    # Отрисовка спрайтов
    screen.blit(dragon.image, dragon.rect)
    screen.blit(coin.image, coin.rect)


    # Проверяем коллизии двух спрайтов
    if dragon.rect.colliderect(coin.rect):
        score += 1
        print(score)
        # Добавим звук
        ...
        # Переместим монетку в случайное место
        coin.rect.x = random.randint(0, WINDOW_WIDTH - coin.rect.width)
        coin.rect.y = ...




    # Обновляем экран
    pg.display.update()
    clock.tick(FPS)

# Выход из игры
pg.quit()