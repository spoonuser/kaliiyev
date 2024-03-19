import datetime
import pygame
pygame.init()
screen = pygame.display.set_mode((829,836))
runer = True
pygame.display.set_caption('Miki Clock')
myfont = pygame.font.Font()
square = pygame.Surface((50,100))
square.fill((219, 22, 101))
clock = pygame.image.load(r"C:\Users\alpam\Downloads\main-clock.png")
lefthand = pygame.image.load(r"C:\Users\alpam\Downloads\left-hand.png")
rightthand = pygame.image.load(r"C:\Users\alpam\Downloads\MicrosoftTeams-image (4).png")
while runer:
    now = datetime.datetime.now()
    s = datetime.datetime.now()
    minutes = now.hour*60 + now.minute
    seconds = s.second
    rotated_image = pygame.transform.rotate(lefthand,-(seconds*6))
    rotated_image2 = pygame.transform.rotate(rightthand,-(minutes*6))
    new_rect = rotated_image.get_rect(center = lefthand.get_rect(topleft = (145,375)).center)
    new_rect2 = rotated_image2.get_rect(center = rightthand.get_rect(topleft = (215,355)).center)
    screen.fill('white')
    screen.blit(clock,(0,0))
    screen.blit(rotated_image2,new_rect2)
    screen.blit(rotated_image,new_rect)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runer = False
            pygame.quit()