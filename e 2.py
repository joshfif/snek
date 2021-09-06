import pygame
import time
import random

pygame.init()

screen = pygame.display.set_mode((702, 702))

pygame.display.set_caption("Snek")

px = 320
py = 320

snakepos = [[320, 320]]

apple = [7 * 64, 5 * 64]

running = True
start = False
first = True
direction = 'none'
waittime = 1

def end():
    for r in range(0, 256):
        screen.fill((r, 255 - r, 0))
        pygame.display.update()
        time.sleep(0.01)
    white = (255, 255, 255)
    green = (0, 255, 0)
    blue = (0, 0, 128)
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render('High Score: ' + str(len(snakepos) - 1), True, green, blue)
    textRect = text.get_rect()
    textRect.center = (351, 351)
    screen.blit(text, textRect)
    pygame.display.update()
    time.sleep(2.5)
    quit()
    

while running:

    screen.fill((0, 255, 0))

    snakenext = snakepos[-1]
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            exit()

        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                if first and direction != 'down':
                    direction = 'up'
                    start = True
                    first = False

            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                if first and direction != 'right':
                    direction = 'left'
                    start = True
                    first = False

            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                if first and direction != 'up':
                    direction = 'down'
                    start = True
                    first = False

            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                if first and direction != 'left':
                    direction = 'right'
                    start = True
                    first = False

            if event.key == pygame.K_f:
                if waittime > 0.25: waittime -= 0.05
                
    first = True
    if start:

        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(apple[0], apple[1], 64, 64))
        
        if direction == 'right': snakenext = [snakenext[0] + 64, snakenext[1]]
        if direction == 'left': snakenext = [snakenext[0] - 64, snakenext[1]]
        if direction == 'up': snakenext = [snakenext[0], snakenext[1] - 64]
        if direction == 'down': snakenext = [snakenext[0], snakenext[1] + 64]

        for n in range(2, len(snakepos)):
            if snakenext == snakepos[n]:
                end()
        snakepos.append(snakenext)

        placeable = False
        if snakenext != apple:
            removed = snakepos[0]
            snakepos.remove(snakepos[0])
        else:
            while not placeable:
                apple = [random.randint(1,10) * 64, random.randint(1,10) * 64]
                not_matching = 0
                for n in range(0, len(snakepos)):
                    if apple != snakepos[n]: not_matching += 1
                if not_matching == len(snakepos):
                    placeable = True
                    
            if waittime > 0.10: waittime -= 0.05

        x = 8  
        for n in range(1, 9):
            screen.fill((0, 255, 0))

            pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(apple[0], apple[1], 64, 64))
            
            for r in range(1, len(snakepos) - 1):
                pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(snakepos[r - 1][0] + (((snakepos[r][0] - snakepos[r - 1][0]) / 8) * n), snakepos[r - 1][1] + (((snakepos[r][1] - snakepos[r - 1][1]) / 8) * n), 64, 64), 2)
                pygame.draw.rect(screen, (255, 215, 0), pygame.Rect((snakepos[r - 1][0] + (((snakepos[r][0] - snakepos[r - 1][0]) / 8) * n)) + 1, (snakepos[r - 1][1] + (((snakepos[r][1] - snakepos[r - 1][1]) / 8) * n)) + 1, 63, 63))

            if direction == "right":
                pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(snakepos[-1][0] - (8 * x), snakepos[-1][1], 64, 64), 2)
                pygame.draw.rect(screen, (255, 255, 0), pygame.Rect((snakepos[-1][0] - (8 * x)) + 1, snakepos[-1][1] + 1, 63, 63))
            if direction == "left":
                pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(snakepos[-1][0] + (8 * x), snakepos[-1][1], 64, 64), 2)
                pygame.draw.rect(screen, (255, 255, 0), pygame.Rect((snakepos[-1][0] + (8 * x)) + 1, snakepos[-1][1] + 1, 63, 63))
            if direction == "up":
                pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(snakepos[-1][0], snakepos[-1][1] + (8 * x), 64, 64), 2)
                pygame.draw.rect(screen, (255, 255, 0), pygame.Rect(snakepos[-1][0] + 1, (snakepos[-1][1] + (8 * x)) + 1, 63, 63))
            if direction == "down":
                pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(snakepos[-1][0], snakepos[-1][1] - (8 * x), 64, 64), 2)
                pygame.draw.rect(screen, (255, 255, 0), pygame.Rect(snakepos[-1][0] + 1, (snakepos[-1][1] - (8 * x)) + 1, 63, 63))
            
            pygame.display.update()
            x -= 1
            time.sleep(waittime / 8)


    pygame.display.update()

    matching = - len(snakepos)

    for n in range(1, len(snakepos)):
        for r in range(1, len(snakepos)):
            if snakepos[n] == snakepos[r]:
                matching += 1
                
        if snakepos[n][0] > 640 or snakepos[n][1] > 640 or snakepos[n][0] < 0 or snakepos[n][1] < 0 or matching > 0:
            running = False
            end()
