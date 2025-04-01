# импортируем все что надо
import pygame
import random
from insert_data import insert_user_data
from insert_data import user_exist
from insert_data import current_level
from insert_data import updating_level

def taking_user_name():
    return input("введите свое имя: ")
pygame.init()
user_name = taking_user_name()
#базовые настройки
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
length = 1
score = 0

#все шрифты все тут настраиваем
font_large = pygame.font.SysFont('Arial', 66, bold=True)
font_small = pygame.font.SysFont('Arial', 26, bold=True)
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
WHITE = (255, 255, 255)
# Скорость
move_i = 0.3  # Начальная задержка
move_t = 0


# Событие для таймера еды
FOOD_TIMEOUT = pygame.USEREVENT + 1
snake = [(x, y)]
class Level():
    def __init__(self, level_num):
        self.blocks = []
        self.block_img = pygame.image.load('tnt.png')
        self.level_num = level_num
        self.locate()
    def locate(self):
        levels = {
            2: [(100,100),],
            3: [(100, 100), (500, 300), (170, 50), (400, 200)],
            4: [(50,400), (300,100)],
            5: [(100,100)]
        }
        positions = levels.get(self.level_num, [])
        for pos in positions:
            rect =self.block_img.get_rect(topleft = pos)
            self.blocks.append(rect)
    def inc_speed(self):
        global move_i
        move_i = max(0.05, float(move_i) - 0.05 * int(self.level_num))




    def draw(self):
        for block in self.blocks:
            screen.blit(self.block_img, block.topleft)

if user_exist(user_name):
    level_num, length = current_level(user_name)
    print(f"Добро пожаловать, {user_name}! Ты продолжаешь с уровня {level_num} и длина змейки у тебя {length}.")
    level = Level(level_num)
    level.inc_speed()
else:
    level_num = 1
    length = 1
    insert_user_data(user_name, level_num,length)
    print(f"Привет, {user_name}! Ты начинаешь с 1 уровня.")
    level = Level(level_num)


#когда вызываем, спавним еду где угодно но не на змейке
def spawn_food():
    while True:
        food = (random.randint(0, WIDTH // snake_size[0] - 1) * snake_size[0],
                random.randint(0, HEIGHT // snake_size[1] - 1) * snake_size[1])
        if food not in snake and not any(block.collidepoint(food) for block in level.blocks):
            return food

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
def game_over():
    global running,final_level
    updating_level(user_name,final_level,length)
    screen.blit(font_large.render("ПОКА", 1, pygame.Color('orange')), (WIDTH // 2 - 100, HEIGHT // 3))
    pygame.display.flip()
    pygame.time.wait(2000)
    pygame.quit()
    exit()

def colision():
        snake_head = pygame.Rect(snake[-1][0], snake[-1][1], snake_size[0], snake_size[1])
        for block in level.blocks:
            if snake_head.colliderect(block):
                game_over()

final_level = level_num
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
    pygame.draw.rect(screen, RED, (food_x, food_y, food_size, food_size))
    pygame.draw.rect(screen, BLUE, (superfood_x, superfood_y, food_size, food_size))
    #рендерим наш score
    screen.blit(font_small.render(f'Score {score}', 1, pygame.Color('orange')), (5, 5))

    level.draw()
    
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
        length += 3
        score += 15

    if score >= level_num * 15:
        level_num +=1
        final_level = level_num
        level= Level(level_num)
        level.inc_speed()
        screen.fill(BLACK)
        screen.blit(font_large.render(f'LEVEL {level_num}', 1, pygame.Color('yellow')), (WIDTH // 2 - 100, HEIGHT // 3))
        pygame.display.flip()
        pygame.time.wait(1000)

    #чекаем колизии
    if (x < 0 or x > WIDTH - snake_size[0] or
            y < 0 or y > HEIGHT - snake_size[1] or
            len(snake) != len(set(snake))):
        game_over()
    #проверяем на колизию с блоками
    colision()

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
