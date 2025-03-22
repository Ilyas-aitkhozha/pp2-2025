import pygame
import datetime

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((1240, 720))

image = pygame.image.load('mickeyclock.png')
image1 = pygame.image.load('min_hand.png')  
image2 = pygame.image.load('right_hand.png')

image = pygame.transform.scale(image, screen.get_size())

pos1 = (620, 360)  
pos2 = (620, 360)  

done = False

def get_angle():
    now = datetime.datetime.now()
    second_angle = -(now.second*6)
    minute_angle = -(now.minute * 6)  
    return second_angle, minute_angle

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    second_angle, minute_angle = get_angle()  

    rotated_image1 = pygame.transform.rotate(image1, minute_angle)
    rotated_image2 = pygame.transform.rotate(image2, second_angle)

    r1_w, r1_h = rotated_image1.get_size()
    r2_w, r2_h = rotated_image2.get_size()

    draw_pos1 = (pos1[0] - r1_w // 2, pos1[1] - r1_h // 2)
    draw_pos2 = (pos2[0] - r2_w // 2, pos2[1] - r2_h // 2)      

    screen.fill((0, 0, 0))  
    screen.blit(image, (0, 0))  
    screen.blit(rotated_image1, draw_pos1)  
    screen.blit(rotated_image2, draw_pos2)  

    pygame.display.flip()  
    clock.tick(1)  

pygame.quit()
