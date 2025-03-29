import pygame
import random

pygame.init()
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
length = 1
score = 0

font_end = pygame.font.SysFont('Arial', 66, bold=True)
font_score = pygame.font.SysFont('Arial', 26, bold=True)

snake_size = (30, 30)
food_size = 10
dirs = {'W': True, 'S': True, 'D': True, 'A': True}

x = WIDTH // 2
y = HEIGHT // 2

GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Скорость
move_i = 0.2  # Начальная задержка
move_t = 0

# Порог для увеличения скорости
next_threshold = 3

def spawn_food():
    return (
        random.randint(0, (WIDTH - food_size) // snake_size[0]) * snake_size[0],
        random.randint(0, (HEIGHT - food_size) // snake_size[1]) * snake_size[1]
    )

food_x, food_y = spawn_food()
snake = [(x, y)]
dx, dy = 0, 0
running = True

while running:
    screen.fill(BLACK)
    dt = clock.tick(144) / 1000
    move_t += dt

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    [pygame.draw.rect(screen, GREEN, (i, j, snake_size[0] - 1, snake_size[1] - 1)) for i, j in snake]
    pygame.draw.rect(screen, RED, (food_x, food_y, food_size, food_size))
    render_score = font_score.render(f'Score {score}', 1, pygame.Color('orange'))
    screen.blit(render_score, (5, 5))

    if move_t > move_i:
        move_t = 0  # Сбрасываем таймер после движения
        x += dx * snake_size[0]
        y += dy * snake_size[1]
        snake.append((x, y))
        snake = snake[-length:]

    if snake[-1] == (food_x, food_y):
        food_x, food_y = spawn_food()
        length += 1
        score += 1

        # Ускоряем змейку при достижении порога
        if score >= next_threshold:
            move_i = max(0.1, move_i - 0.05)  # Уменьшаем интервал
            next_threshold += 3  # Следующий порог

    if (x < 0 or x > WIDTH - snake_size[0] or
            y < 0 or y > HEIGHT - snake_size[1] or
            len(snake) != len(set(snake))):
        render_end = font_end.render("ПОКА", 1, pygame.Color('orange'))
        screen.blit(render_end, (WIDTH // 2 - 100, HEIGHT // 3))
        pygame.display.flip()
        pygame.time.wait(2000)
        running = False

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_w] and dirs['W']:
        dx, dy = 0, -1
        dirs = {'W': True, 'S': False, 'D': True, 'A': True}
    elif pressed[pygame.K_s] and dirs['S']:
        dx, dy = 0, 1
        dirs = {'W': False, 'S': True, 'D': True, 'A': True}
    elif pressed[pygame.K_d] and dirs['D']:
        dx, dy = 1, 0
        dirs = {'W': True, 'S': True, 'D': True, 'A': False}
    elif pressed[pygame.K_a] and dirs['A']:
        dx, dy = -1, 0
        dirs = {'W': True, 'S': True, 'D': False, 'A': True}

    pygame.display.flip()
