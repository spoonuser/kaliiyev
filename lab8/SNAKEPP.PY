import pygame
import random
pygame.init()
RES = 600
SIZE = 50
screen = pygame.display.set_mode((RES,RES))
x,y = random.randrange(0,RES,SIZE), random.randrange(0,RES,SIZE)
apple = random.randrange(0,RES,SIZE),random.randrange(0,RES,SIZE)
baff = random.randrange(0,RES,SIZE),random.randrange(0,RES,SIZE)
over = pygame.image.load(r"C:\Users\alpam\Downloads\31.03.2024 21_02_29.png")#gameover.png
length = 1
snake = [(x,y)]
dx,dy = 0,0
fps = 6
shrink = 50
runer = True 
color = (0, 153, 230)
stop = True
while runer:
    screen.fill("black")
    clock = pygame.time.Clock()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runer = False
            pygame.quit()
            break
        elif  event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                dx,dy = 0, -1
            elif event.key == pygame.K_a:
                dx,dy = -1, 0
            elif event.key == pygame.K_s:
                dx,dy = 0, 1
            elif event.key == pygame.K_d:
                dx,dy = 1, 0 
    if stop:
        [(pygame.draw.rect(screen,"green", (i, j, SIZE, SIZE))) for i,j in snake]
        pygame.draw.rect(screen,"red", (*apple,SIZE,SIZE))
        x = x + dx *SIZE
        y = y + dy *SIZE
        snake.append((x, y))
        snake = snake[-length:]
        if length % 3 == 0:
            pygame.draw.rect(screen,"blue", (*baff,SIZE,SIZE))
            if snake[-1]== baff:
                length = length + 2
                fps = fps - 2
                baff = random.randrange(0,RES,SIZE),random.randrange(0,RES,SIZE)
        if snake[-1]== apple:
            apple = random.randrange(0,RES-100,SIZE),random.randrange(0,RES-100,SIZE)
            length = length + 1
            fps = fps + 1
    if x < 0 or  x > RES - SIZE  or y < 0 or y > RES- SIZE:
        stop = False
        screen.blit(over,(-130,0))
    if len(snake) != len(set(snake)):
        stop = False
        screen.blit(over,(-130,0))
    pygame.display.update()
    clock.tick(fps)
