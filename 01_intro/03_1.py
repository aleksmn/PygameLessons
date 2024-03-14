import pygame as pg

size = (800, 800)
screen = pg.display.set_mode(size)
# Заголовок окна
pg.display.set_caption('Движение')

# Создадим прямоугольник
small_rect = pg.Rect(0, 0, 60, 30)

# изменяем размеры прямоугольника
small_rect.size = (100, 100)

# изменяем расположение прямоугольника
small_rect.center = (size[0]//2, size[1]//2)


direction = 'left'

# Задаем FPS
fps = 60
clock = pg.time.Clock()


# Игровой цикл
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    #--------------------------- 

    # Изменяем размер
    # small_rect.width += 1
    # small_rect.height += 1
    # small_rect.center = size[0]/2, size[1]/2
            
    # Движение

    if small_rect.right == size[0]:      
        direction = "left"
    if small_rect.left == 0:
        direction = "right"

    if direction == "right":
        small_rect.x += 1
    if direction == "left":
        small_rect.x -= 1
     



    # Заливка фона
    screen.fill("cyan")
    
    # Отрисовка прямоугольника
    pg.draw.rect(screen, "orange", small_rect)


    # Переключаем кадр
    pg.display.flip()
    clock.tick(fps)


pg.quit()