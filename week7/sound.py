import pygame
import pygame.mixer
_songs = ['ambient-128950.mp3', 'background-horror-tension-171540.mp3', 'desolate-150576.mp3', 'energetic-background-for-happy-moments-30s-248827.mp3', 'horror-background-atmosphere-15-246917.mp3']

def play_next_song():
    global _songs
    _songs = _songs[1:] + [_songs[0]] 
    pygame.mixer.music.load(_songs[0])
    pygame.mixer.music.play()

def play_previous_song():
    global _songs
    if _songs:
        _songs = [_songs[-1]] + _songs[:-1]
        pygame.mixer.music.load(_songs[0])
        pygame.mixer.music.play()


pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((1240, 720))
done = False
is_playing = False
font = pygame.font.Font(None, 62)
font1 = pygame.font.Font(None, 42)
font2 = pygame.font.Font(None, 42)
space = pygame.image.load('space.png')
space = pygame.transform.scale(space, (800,220))
R_arrow = pygame.image.load('R_arrow.png')
R_arrow = pygame.transform.scale(R_arrow, (400,180))
L_arrow = pygame.image.load('L_arrow.png')
L_arrow = pygame.transform.scale(L_arrow, (400,180))
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                      play_next_song()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                      if not is_playing:
                            pygame.mixer.music.load(_songs[0])
                            pygame.mixer.music.play()
                            is_playing = True
                      else:
                            if pygame.mixer.music.get_busy():
                                  pygame.mixer.music.pause()
                            else:
                                  pygame.mixer.music.unpause()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                      play_previous_song()
        screen.fill((0,0,0))
        screen.blit(space, (220, 90))    
        screen.blit(R_arrow, (700, 420))
        screen.blit(L_arrow, (100, 420))
        text = font.render("Press SPACE to Play or Pause", True, (255, 255, 255)) 
        screen.blit(text, (300, 40))
        text1 = font1.render("Press LEFT Key to play next song", True, (255,255,255))
        screen.blit(text1, (70, 370))
        text2 = font2.render("Press RIGHT Key to play next song", True, (255,255,255))
        screen.blit(text2, (670, 370))
        pygame.display.flip()