import pygame
import sys
import math

# Инициализация Pygame
pygame.init()

# Константы
WIDTH, HEIGHT = 800, 600
FPS = 60
SUN_RADIUS = 50
PLANET_RADIUS = 15
PLANET_ORBIT_RADIUS = 150

# Цвета
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
GRAY = (169, 169, 169)
ORANGE = (255, 165, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BROWN = (139, 69, 19)
GOLD = (255, 215, 0)
CYAN = (0, 255, 255)

# Окно
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Симулятор солнечной системы")
clock = pygame.time.Clock()

class Planet:
    def __init__(self, color, radius, orbit_radius, speed):
        self.color = color
        self.radius = radius
        self.orbit_radius = orbit_radius
        self.angle = 0
        self.speed = speed

    def update(self):
        self.angle += self.speed

    def draw(self):
        x = int(WIDTH / 2 + self.orbit_radius * math.cos(math.radians(self.angle)))
        y = int(HEIGHT / 2 + self.orbit_radius * math.sin(math.radians(self.angle)))
        pygame.draw.circle(screen, self.color, (x, y), self.radius)

# Создание планет
mercury = Planet(GRAY, PLANET_RADIUS, PLANET_ORBIT_RADIUS * 0.4, 1)
venus = Planet(ORANGE, PLANET_RADIUS, PLANET_ORBIT_RADIUS * 0.7, 0.8)
earth = Planet(BLUE, PLANET_RADIUS, PLANET_ORBIT_RADIUS, 0.5)
mars = Planet(RED, PLANET_RADIUS, PLANET_ORBIT_RADIUS * 1.5, 0.2)
jupiter = Planet(BROWN, PLANET_RADIUS, PLANET_ORBIT_RADIUS * 2, 0.1)
saturn = Planet(GOLD, PLANET_RADIUS, PLANET_ORBIT_RADIUS * 2.7, 0.07)
uranus = Planet(CYAN, PLANET_RADIUS, PLANET_ORBIT_RADIUS * 3.5, 0.05)
neptune = Planet(BLUE, PLANET_RADIUS, PLANET_ORBIT_RADIUS * 4.2, 0.03)

planets = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]

# Основной цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Очистка экрана
    screen.fill(WHITE)

    # Рисование солнца
    pygame.draw.circle(screen, YELLOW, (int(WIDTH / 2), int(HEIGHT / 2)), SUN_RADIUS)

    # Обновление и рисование планет
    for planet in planets:
        planet.update()
        planet.draw()

    # Обновление экрана
    pygame.display.flip()

    # Задержка для достижения нужного FPS
    clock.tick(FPS)