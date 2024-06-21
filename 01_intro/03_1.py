import pygame as pg

size = (800, 800)
screen = pg.display.set_mode(size)

# Заголовок окна
pg.display.set_caption('Движение')

# Создадим прямоугольник
#                   (x, y, w, h)
small_rect = pg.Rect(0, 0, 60, 30)

# изменяем размеры прямоугольника
# small_rect.size = (100, 100)
small_rect.width = 100
small_rect.height = 100

# изменяем расположение прямоугольника
small_rect.center = (size[0]//2, size[1]//2)

direction = "left"

# Задаем FPS
fps = 60
clock = pg.time.Clock()

# Игровой цикл
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                direction = "left"
            if event.key == pg.K_RIGHT:
                direction = "right"
            if event.key == pg.K_UP:
                direction = "up"
            if event.key == pg.K_DOWN:
                direction = "down"

    # Заливка фона
    screen.fill("cyan")


    # Отскок от стены
    if small_rect.right == size[0]:
        direction = "left"        
    if small_rect.left == 0:
        direction = "right"
    if small_rect.top == 0:
        direction = "down"
    if small_rect.bottom == size[0]:
        direction = "up"  


    if direction == "right":
        small_rect.x += 1
    if direction == "left":
        small_rect.x -= 1
    if direction == "up":
        small_rect.y -= 1
    if direction == "down":
        small_rect.y += 1

    # Отрисовка прямоугольника
    pg.draw.rect(screen, "orange", small_rect)






    # Переключаем кадр
    pg.display.flip()
    clock.tick(fps)
# Все что выше - внутри цикла while
pg.quit()