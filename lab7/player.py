import pygame
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((512,512))
screen.fill("white") 
counter = 0
runer = True
index = 0
pauseicon = pygame.image.load(r"C:\Users\alpam\Downloads\9034391_resume_icon.png")
resumeicon = pygame.image.load(r"C:\Users\alpam\Downloads\809530_media control_multimedia_pause_icon.png")
playlist = [r"C:\Users\alpam\Desktop\songs\Metallica - Master Of Puppets.mp3",
            r"C:\Users\alpam\Desktop\songs\MGMT - Little Dark Age.mp3",
            r"C:\Users\alpam\Desktop\songs\Metallica - Nothing Else Matters.mp3",
            r"C:\Users\alpam\Desktop\songs\Eminem & Dido - Stan.mp3",
            r"C:\Users\alpam\Desktop\songs\Muse - The 2nd Law Isolated System.mp3",
            r"C:\Users\alpam\Desktop\songs\Smash Mouth - All Star.mp3",
            r"C:\Users\alpam\Desktop\songs\Виктор Цой - Звезда по имени Солнце.mp3"
            r"C:\Users\alpam\Desktop\songs\Виктор Цой - Звезда по имени Солнце.mp3"
            ]
pygame.mixer.music.load(playlist[index])
pygame.mixer.music.play()
screen.blit(resumeicon,(0,0)) 
pause = True
while runer:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pause = not pause
            if event.key == pygame.K_d:
                index = index + 1
                pygame.mixer.music.load(playlist[index])
                pygame.mixer.music.play()
            if event.key == pygame.K_a:
                index = index - 1
                pygame.mixer.music.load(playlist[index])
                pygame.mixer.music.play()
            if pause == False:
                pygame.mixer.music.pause()
                screen.fill("white") 
                screen.blit(pauseicon,(0,0))
            if pause == True:
                pygame.mixer.music.unpause()
                screen.fill("white") 
                screen.blit(resumeicon,(0,0))  
        if event.type == pygame.QUIT:
            runer = False
            pygame.quit()
            break
#Space --> pause/unpause
#A --> previous song
#D --> next song          