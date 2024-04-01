import pygame
import random
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((600,600))
runer = True
pygame.display.set_caption('First project')
square = pygame.Surface((50,100))
square.fill((219, 22, 101))
square = pygame.Surface((50,100))
ButtonD = False
ButtonA = False
a = 300
b = 500
c = 15
d = 0
x,y = 0,0
game = True
players_car = pygame.image.load(r"C:\Users\alpam\Downloads\31.03.2024 18_35_42.png")#playercar.png
enemy_car = pygame.image.load(r"C:\Users\alpam\Downloads\31.03.2024 19_41_07.png")#enemycar.png
road = pygame.image.load(r"C:\Users\alpam\Pictures\photo_2024-03-31_19-56-23.jpg")#road.jpg
over = pygame.image.load(r"C:\Users\alpam\Downloads\31.03.2024 21_02_29.png")#gameover.png
coinn = pygame.image.load(r"C:\Users\alpam\Pictures\31.03.2024 20_11_31.png")#coin.png
start_time = pygame.time.get_ticks()
start_time2 = pygame.time.get_ticks()
state = pygame.key.get_pressed()
balls = []
coins = []
score = 0
font_score = pygame.font.SysFont('Arial' , 26 , bold = True)
pygame.mixer.music.load(r"C:\Users\alpam\Music\Coin_Pick.mp3")#Coin_Pick.mp3
while runer:
    if game:
        screen.blit(road,(0,0))
        render_score = font_score.render(f'Your score: {score}',1,'Black')
        screen.blit(render_score , (400,0))
    if game:
        if pygame.time.get_ticks()-start_time>1000:
            random_int1 = random.randrange(450)
            balls.append([random_int1,0])
            start_time = pygame.time.get_ticks()
    if game:
        for ball in balls:
            screen.blit(enemy_car,(ball[0],ball[1]))
            ball[1] = ball[1] + 5
    if pygame.time.get_ticks()-start_time2>3300:
            random_int2 = random.randrange(450)
            coins.append([random_int2,0])
            start_time2 = pygame.time.get_ticks()
    if game:
        for coin in coins:
            screen.blit(coinn,(coin[0],coin[1]))
            coin[1] = coin[1] + 5
    
    clock.tick(100)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    if game:
        screen.blit(players_car,(a,b))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runer = False
            pygame.quit()
            break
    state = pygame.key.get_pressed()            
    if state[pygame.K_RIGHT]:
        if a < 500:
            a = a + c
    if state[pygame.K_LEFT]:
        if a > 20:
            a = a - c
    for ball in balls:
        if abs(a-ball[0])<=40 and abs(b-ball[1]) <=40:
            game = False
            screen.blit(over,(-130,0))
            screen.blit(render_score , (400,0))
            pygame.display.update
            c = 0
    for coin in coins:
        if abs(a-coin[0])<=50 and abs(b-coin[1]) <=50:
            pygame.mixer.music.play()
            coin[0] = 1000
            score = score + 1
            pygame.display.update
    pygame.display.update()
        
        
        
