import pygame
pygame.init()
screen = pygame.display.set_mode((1200,900))
runer = True
pygame.display.set_caption('First project')
square = pygame.Surface((50,100))
square.fill((219, 22, 101))
square = pygame.Surface((50,100))
square.fill((219, 22, 101))
ButtonD = False
ButtonW = False
ButtonA = False
ButtonS = False
a = 50
b = 50
c = 20
state = pygame.key.get_pressed()
clock = pygame.time.Clock()
while runer:
    
    screen.fill('black')
    pygame.draw.circle(screen,'Red',(a,b),50)
    pygame.display.update()
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runer = False
            pygame.quit()
            break
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if a < 1150:
                    a = a + 20
            elif event.key == pygame.K_LEFT:
                if a > 50:
                    a = a - 20
            elif event.key == pygame.K_UP:
                if b > 50:
                    b = b - 20
            elif event.key == pygame.K_DOWN:
                if b < 850:
                    b = b + 20
    state = pygame.key.get_pressed()            
    if state[pygame.K_RIGHT]:
        if a < 1150:
            a = a + c
    if state[pygame.K_LEFT]:
        if a > 50:
            a = a - c
    if state[pygame.K_UP]:
        if b > 50:
            b = b - c
    if state[pygame.K_DOWN]:
        if b < 850:
            b = b + c