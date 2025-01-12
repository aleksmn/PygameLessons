import pygame as pg

# Размер окна
size = (500, 500)
screen = pg.display.set_mode(size)
# Заголовок окна
pg.display.set_caption('Движение прямоугольника')


small_rect = pg.Rect(0, 0, 60, 30)

# Меняяем размеры
small_rect.width = 100
small_rect.height = 100

# Меняем расположение
small_rect.x = size[0]//2 - small_rect.width // 2
small_rect.y = size[1]//2 - small_rect.height // 2


direction = 1


# FPS
fps = 60
clock = pg.time.Clock()

running = True
# Игровой цикл
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    
    # Заливка фона
    screen.fill("orange")

    # Отскок от стены
    if small_rect.left == 0:
        direction = 1
    if small_rect.right == size[0]:
        direction = -1



    small_rect.x += direction


    # Отрисовка прямоугольника
    pg.draw.rect(screen, "aqua", small_rect)



    # Переключаем кадр
    pg.display.flip()
    clock.tick(fps)

# Завершение работы
pg.quit()