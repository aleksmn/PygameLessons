import pygame as pg

from sprites import Character, Butterfly


# Инициализируем модуль для проигрывания звуков
pg.mixer.init()

# Размер окна
size = (500, 500)
screen = pg.display.set_mode(size)
# Заголовок окна
pg.display.set_caption('Обработка событий')

fps = 60
clock = pg.time.Clock()

background = pg.image.load("images/background.png")
background = pg.transform.scale(background, size)

character = Character()
# Создаем группу спрайтов
butterflies = pg.sprite.Group()
# Добавляем спрайты в группу
for _ in range(5):
    butterflies.add(Butterfly())


running = True
while running:
    for event in pg.event.get():

        if event.type == pg.QUIT:
            running = False

    character.update()
    butterflies.update()

    screen.blit(background, (0, 0))

    # Отрисовка персонажа
    screen.blit(character.image, character.rect)

    butterflies.draw(screen)

    
    pg.display.flip()
    clock.tick(fps)

pg.quit()
