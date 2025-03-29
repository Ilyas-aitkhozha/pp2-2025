#импортируем все необходимые библиотеки
import pygame, sys
from pygame.locals import *
import random, time
#просим инпут от пользователя что бы узнать, на каком n надо увеличивать скорость врагов
N = int(input("Gimme your N"))

pygame.init()

#поставили фпс 60, при 144 слишком быстро при 30 слишком медленно
FPS = 60
FramePerSec = pygame.time.Clock()

#закрэйтили все колоры которые нам понадобятся
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
#базовые параметры
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
ENEMY_SPEED = 5 # для того что бы изменять именно врага скорость, (нужна для фичи с увелечением при достижении N)
SPEED = 5 # Базовая скорость игры для всех кроме врагов
SCORE = 0 # будет отображать от скольких челов увернулись
SCORE_COINS = 0 # скок капибар или кошечек собрали
 
#все шрифты прописаны здесь, рендерим game_over здесь, потому что оно буедт вызываться только один раз
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
 
background = pygame.image.load("AnimatedStreet.png")
 
#просто белый экран(400,600)
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

#первый класс, коины, тут будут прописаны все их методы

class Coins(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image_capy = pygame.image.load("capybara.png")
        self.image_kitten = pygame.image.load("kitten.png")
        self.respawn()
    
    
    def move(self):
        self.rect.move_ip(0, SPEED // 2)  # Коины падают медленнее врагов
        if self.rect.top > SCREEN_HEIGHT: #как задели низ, обратно респавним
            self.respawn()

    def respawn(self):
        if random.choice([True,False]): #здесь на рандом выбираем TRUE ИЛИ FALSE, нужно что бы наугад выбрать какой будет следующий коин
            self.current_image = self.image_capy
            self.value = 1 # если капибара то +1 к скору
        else:
            self.current_image = self.image_kitten
            self.value = 3 # если киттен то +3 к скору
        self.rect = self.current_image.get_rect(center=(random.randint(40, SCREEN_WIDTH - 40), random.randint(-200, -50)))
        #тут просто делаем прямоугольник вокруг картинки, для понимания когда он коснется с игроком
 
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)  
 
      def move(self):
        global SCORE
        self.rect.move_ip(0,ENEMY_SPEED) # изменяем чисто для противника 
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
 
 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
       #if pressed_keys[K_UP]:
            #self.rect.move_ip(0, -5)
       #if pressed_keys[K_DOWN]:
            #self.rect.move_ip(0,5)
         
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0) # муваем в лево 
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0) # муваем вправо
                   
#делаем спрайты       
P1 = Player()
E1 = Enemy()
C1 = Coins()
 
#создаем спрайт групы
coins = pygame.sprite.Group()
coins.add(C1)
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)
 
#создаем свой юзерский ивент, даем уникальный номер (1), каждую секунду будет добавляться скорость 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)
 

while True:
       
    #чекаем все ивенты
    for event in pygame.event.get():
        if event.type == INC_SPEED: # если наш юзерский, увеличваем скорость на 0.5
            SPEED += 0.5
        if event.type == QUIT: # если quit ну тогда выходим
            pygame.quit()
            sys.exit()
    #обновлять  фон (blit принимает два аргумента, то что надо обновить и где это сделать (координаты))
    DISPLAYSURF.blit(background, (0,0))
    #для скора в левом верхнем углу
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))
    #для скора коинов в правом верхнем углу
    scores = font_small.render(str(SCORE_COINS), True, BLACK)
    DISPLAYSURF.blit(scores, (350,10))
 
    #муваем наши спрайты, отдельное условие для коинов, так как там current image(из за рандома)
    for entity in all_sprites:
        if isinstance(entity, Coins):  # Если объект - коин
            DISPLAYSURF.blit(entity.current_image, entity.rect)
            entity.move()
        else:
            DISPLAYSURF.blit(entity.image, entity.rect)
            entity.move()
    # чекаем на то коснулись ли наши ректанглы между друг другом, если плэйер с коином, зарабатываем score 
    if pygame.sprite.spritecollideany(P1, coins):
        for coin in coins:
            if P1.rect.colliderect(coin.rect):  # Проверяем конкретный коин
                SCORE_COINS += coin.value  # Добавляем нужное значение
                pygame.mixer.Sound('for_coins.mp3').play()
                coin.respawn()  # Респавним коин
    # если достигли N или больше,  который дал нам юзер, увеличваем скорость врага
    if SCORE_COINS >= N:
        ENEMY_SPEED = 13
        

    #если случилось столкновение между плэйером и врагом, то выводим gameover 
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound('crash.wav').play()
          time.sleep(0.5)
                    
          DISPLAYSURF.fill(RED)
          DISPLAYSURF.blit(game_over, (30,250))
           
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() #удаляем все спрайты
          time.sleep(2) # через 2 сек выходим
          pygame.quit()
          sys.exit()        
         
    pygame.display.update()
    FramePerSec.tick(FPS)