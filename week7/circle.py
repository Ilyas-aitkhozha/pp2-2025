import pygame

pygame.init()
screen = pygame.display.set_mode((400, 200))
done = False
color = (255, 0, 0)
radius = 25
x = 100
y = 100
clock = pygame.time.Clock()
while not done:
        fps = clock.tick(144)/1000
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RIGHT:
                              x = min(400 - radius, x + 20)
                        if event.key == pygame.K_LEFT:
                              x = max(radius, x - 20)
                        if event.key == pygame.K_UP:
                               y = max(radius, y - 20)
                        if event.key == pygame.K_DOWN:
                               y = min(200 - radius, y + 20)

        screen.fill((255,255,255))
        pygame.draw.circle(screen, color, (x, y), radius)
        
        pygame.display.flip()
        clock.tick(144)
