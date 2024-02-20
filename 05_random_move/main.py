import pygame
import sys
import random

pygame.init()

# Определение цветов
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class Sprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (400, 300)
        self.target_x = random.randint(0, 800)
        self.target_y = random.randint(0, 600)
        self.easing_factor = 0.01
        self.change_direction_time = random.randint(1, 5) * 100
        self.last_direction_change = pygame.time.get_ticks()

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_direction_change > self.change_direction_time:
            self.target_x = random.randint(0, 800)
            self.target_y = random.randint(0, 600)
            # self.change_direction_time = random.randint(1, 5) * 1000
            self.change_direction_time = random.randint(1, 5) * 100
            self.last_direction_change = now

        self.rect.x += (self.target_x - self.rect.x) * self.easing_factor
        self.rect.y += (self.target_y - self.rect.y) * self.easing_factor

# Создание окна игры
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Спрайт Pygame с плавным перемещением")

# Создание группы спрайтов и добавление спрайта в нее
all_sprites = pygame.sprite.Group()
sprite = Sprite()
all_sprites.add(sprite)

clock = pygame.time.Clock()

# Главный игровой цикл
while True:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    all_sprites.update()
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(60)