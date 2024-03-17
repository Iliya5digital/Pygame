import pygame
import sys

# Инициализация Pygame
pygame.init()

# Установка размеров экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Следование мыши")

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Размеры и скорость квадрата
square_size = 50
square_speed = 5

# Начальное положение квадрата
square_x = SCREEN_WIDTH // 2 - square_size // 2
square_y = SCREEN_HEIGHT // 2 - square_size // 2

# Основной цикл программы
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Получение текущего положения мыши
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Расчет нового положения квадрата
    if abs(mouse_x - square_x) > square_speed:
        if mouse_x > square_x:
            square_x += square_speed
        else:
            square_x -= square_speed

    if abs(mouse_y - square_y) > square_speed:
        if mouse_y > square_y:
            square_y += square_speed
        else:
            square_y -= square_speed

    # Отрисовка
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, (square_x, square_y, square_size, square_size))

    # Обновление экрана
    pygame.display.flip()

    # Задержка для контроля частоты обновления кадров
    pygame.time.Clock().tick(60)

# Выход из Pygame
pygame.quit()
sys.exit()
