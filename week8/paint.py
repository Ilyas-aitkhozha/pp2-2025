import pygame

# экран
screen = pygame.display.set_mode((900, 700))
screen.fill((255, 255, 255))

# название
pygame.display.set_caption('GFG Paint')

draw_on = False
last_pos = (0, 0)
radius = 5

# цвет
WHITE = (255 ,255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (102, 204, 0)
BLUE = (51, 51, 255)
BLACK = (0, 0, 0)
PINK = (255, 0, 255)
color = BLACK  # Цвет по умолчанию

# цвета на экране
pygame.draw.rect(screen, RED, (0, 50, 20, 20))
pygame.draw.rect(screen, YELLOW, (0, 70, 20, 20))
pygame.draw.rect(screen, GREEN, (20, 50, 20, 20))
pygame.draw.rect(screen, BLUE, (20, 70, 20, 20))
pygame.draw.rect(screen, BLACK, (0, 90, 20, 20))
pygame.draw.rect(screen, PINK, (20, 90, 20, 20))
erasor = pygame.transform.scale(pygame.image.load('eraser.png'), (40, 40))
screen.blit(erasor, [0, 110])

def roundline(canvas, color, start, end, radius=1):
    Xaxis = end[0] - start[0]   
    Yaxis = end[1] - start[1]
    dist = max(abs(Xaxis), abs(Yaxis))
    for i in range(dist):
        x = int(start[0] + float(i) / dist * Xaxis)
        y = int(start[1] + float(i) / dist * Yaxis)
        pygame.draw.circle(canvas, color, (x, y), radius)

try:
    while True:
        e = pygame.event.wait()

        if e.type == pygame.QUIT:
            raise StopIteration
        key = pygame.key.get_pressed()
        if e.type == pygame.MOUSEBUTTONDOWN:
            spot = pygame.mouse.get_pos()
            if spot[0] < 20 and 50 < spot[1] < 70:
                color = RED
            elif 20 < spot[0] < 40 and 50 < spot[1] < 70:
                color = GREEN
            elif spot[0] < 20 and 70 < spot[1] < 90:
                color = YELLOW
            elif 20 < spot[0] < 40 and 70 < spot[1] < 90:
                color = BLUE
            elif spot[0] < 20 and 90 < spot[1] < 110:
                color = BLACK
            elif 20 < spot[0] < 40 and 90 < spot[1] < 110:
                color = PINK
            elif spot[0] < 40 and 110 < spot[1] < 150:
                color = WHITE

            if spot[0] > 60:
                pygame.draw.circle(screen, color, e.pos, radius)
            draw_on = True
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_w:
                radius += 20  # Теперь изменение радиуса работает корректно
            if e.key == pygame.K_s:
                radius -=20

        if e.type == pygame.MOUSEBUTTONUP:
            draw_on = False
        
        if e.type == pygame.MOUSEMOTION:
            spot = pygame.mouse.get_pos()
            if draw_on and spot[0] > 60:
                pygame.draw.circle(screen, color, e.pos, radius)
                roundline(screen, color, e.pos, last_pos, radius)
            last_pos = e.pos

        if e.type == pygame.KEYDOWN:
            spot = pygame.mouse.get_pos()
            if spot:  # Проверяем, что мышь находится в окне
                if e.key == pygame.K_r:
                    rect_size = 100
                    pygame.draw.rect(screen, color, (spot[0], spot[1], rect_size, rect_size + 100))
                elif e.key == pygame.K_c:
                    circle_radius = 50
                    pygame.draw.circle(screen, color, (spot[0], spot[1]), circle_radius)

        pygame.display.flip()

except StopIteration:
    pass

pygame.quit()
