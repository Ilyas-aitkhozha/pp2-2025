# импортируем все что надо
import pygame
import random
pygame.init()
#базовые настройки
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
length = 1
score = 0

#все шрифты все тут настраиваем
font_end = pygame.font.SysFont('Arial', 66, bold=True)
font_score = pygame.font.SysFont('Arial', 26, bold=True)


snake_size = (30, 30)
food_size = 10

#словарь для чека нашего направления, (если идем на вверх то вниз будет false)
dirs = {'W': True, 'S': True, 'D': True, 'A': True}

x = WIDTH // 2
y = HEIGHT // 2
BLUE = (0,0,255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Скорость
move_i = 0.2  # Начальная задержка
move_t = 0

# Порог для увеличения скорости
next_threshold = 3
# Событие для таймера еды
FOOD_TIMEOUT = pygame.USEREVENT + 1

#когда вызываем, спавним еду где угодно но не на змейке
def spawn_food():
    return (
        random.randint(0, (WIDTH - food_size) // snake_size[0]) * snake_size[0],
        random.randint(0, (HEIGHT - food_size) // snake_size[1]) * snake_size[1]
    )

#спавним обычную и супер еду(+1 для обычной, +3 для супер)
food_x, food_y = spawn_food()
superfood_x, superfood_y = spawn_food()

#нужно что бы исчезал спустя 3 сек
pygame.time.set_timer(FOOD_TIMEOUT, 3000)
#координаты змейки
snake = [(x, y)]
#наши направление , к примеру (0, -1 вверх), (1, 0 вправо)
dx, dy = 0, 0
running = True

while running:
    screen.fill(BLACK)
    dt = clock.tick(144) / 1000 #хранит разницу во времени между кадрами
    move_t += dt# суммирует их(что бы контролировать скорость движения змейки)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == FOOD_TIMEOUT:#чекаем нащ юзерский ивент
            food_x, food_y = spawn_food()
            superfood_x, superfood_y = spawn_food()
            pygame.time.set_timer(FOOD_TIMEOUT, 3000)  # Перезапускаем таймер

    for i, j in snake: # рисуем змеечку
       pygame.draw.rect(screen, GREEN, (i, j, snake_size[0] - 1, snake_size[1] - 1))

    #рисуем еду
    pygame.draw.rect(screen, RED, (food_x, food_y, food_size, food_size))
    pygame.draw.rect(screen, BLUE, (superfood_x, superfood_y, food_size, food_size))
    #рендерим наш score
    render_score = font_score.render(f'Score {score}', 1, pygame.Color('orange'))
    screen.blit(render_score, (5, 5))
    #если move_t накопил больше чем move_i то змейка двигается
    if move_t > move_i:
        move_t = 0  # Сбрасываем таймер после движения
        x += dx * snake_size[0]
        y += dy * snake_size[1]
        snake.append((x, y))
        snake = snake[-length:]#каждый раз удаляем последний сегмент если не сьела ничего, т.к иначе будет бесконечной
    

    if snake[-1] == (food_x, food_y):#если коснулась, то едим, добавляем score (для супер еды +3 score)
        food_x, food_y = spawn_food()
        length += 1
        score += 1
    if snake[-1] == (superfood_x, superfood_y):
        superfood_x, superfood_y = spawn_food()
        length += 1
        score += 3

        # Ускоряем змейку при достижении порога
        if score >= next_threshold:
            move_i = max(0.1, move_i - 0.05)  # Уменьшаем интервал
            next_threshold += 3  # Следующий порог

    if (x < 0 or x > WIDTH - snake_size[0] or
            y < 0 or y > HEIGHT - snake_size[1] or
            len(snake) != len(set(snake))):#проверяем если коснулись границ, или самого себя то тогда gameover
        render_end = font_end.render("ПОКА", 1, pygame.Color('orange'))
        screen.blit(render_end, (WIDTH // 2 - 100, HEIGHT // 3))
        pygame.display.flip()
        pygame.time.wait(2000)
        running = False

    #кнопки управления
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
