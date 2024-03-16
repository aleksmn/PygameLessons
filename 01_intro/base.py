import pygame as pg

# Размер окна
size = (500, 500)
screen = pg.display.set_mode(size)
# Заголовок окна
pg.display.set_caption('Заголовок окна')




# FPS
fps = 100
clock = pg.time.Clock()

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    
    # Заливка фона
    screen.fill("orange")

    # Переключаем кадр
    pg.display.flip()
    clock.tick(fps)

# Завершение работы
pg.quit()