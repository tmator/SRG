#pip install pygame pypiwin32
import pyHook
import pygame
import subprocess
import os
import sys

white = (255, 255, 255)
green = (0, 255, 0)

selected = 0

done = False
# Initialize Pygame
pygame.init()
clock = pygame.time.Clock()

#font = pygame.font.SysFont("comicsansms", 72)
font = pygame.font.Font('freesansbold.ttf', 32)
font2= pygame.font.Font('freesansbold.ttf', 20)


text = font.render('Sega Racing', True, white)
text0 = font2.render('Pressez le bouton View change pour selectionner un jeu puis Start pour demarrer. Pour revenir au menu pressez 5 secondes sur Start.', True, white)

text1 = font.render('1P Daytona USA', True, green)
text2 = font.render('1P Sega Rally', True, white)
text3 = font.render('2P Daytona USA', True, white)
text4 = font.render('2P Sega Rally', True, white)
text10 = font.render('Quitter', True, white)


# Set the screen to fullscreen
#screen = pygame.display.set_mode((1920, 1080))
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)


# Start the main loop
while not done:

    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
                subprocess.Popen("shutdown /s")
                pygame.quit()
                
            if event.key == pygame.K_DOWN:
                if (selected < 4):
                    selected+=1
                else:
                    selected=0
                    
            if event.key == pygame.K_s:
                #start game
                pygame. display. toggle_fullscreen()
                if (selected==0):
                    os.chdir("C:\m2emulator")
                    subprocess.Popen("emulator_multicpu.exe dayton93")
                if (selected==1):
                    os.chdir("C:\m2emulator")
                    subprocess.Popen("emulator_multicpu.exe srallycb")
                if (selected==2):
                    os.chdir("C:\m2emulator_multi")
                    subprocess.Popen("emulator_multicpu.exe daytona")
                if (selected==3):
                    os.chdir("C:\m2emulator_multi")
                    subprocess.Popen("emulator_multicpu.exe srallycb")
                if (selected==4):
                    done = True
                    subprocess.Popen("shutdown /s")
                    pygame.quit()
                #print("launch ok ", selected)
                done = True
                pygame.quit()
                sys.exit()
                
        # Check for the quit event
        
        
        if event.type == pygame.QUIT:
            # Quit the game
            done = True
            pygame.quit()
            sys.exit()
            
            
            
        if (selected == 0):
            text1 = font.render('1P Daytona USA', True, green)
            text2 = font.render('1P Sega Rally', True, white)
            text3 = font.render('2P Daytona USA', True, white)
            text4 = font.render('2P Sega Rally', True, white)
            text10 = font.render('Quitter', True, white)
        if (selected == 1):
            text1 = font.render('1P Daytona USA', True, white)
            text2 = font.render('1P Sega Rally', True, green)
            text3 = font.render('2P Daytona USA', True, white)
            text4 = font.render('2P Sega Rally', True, white)
            text10 = font.render('Quitter', True, white)
        if (selected == 2):
            text1 = font.render('1P Daytona USA', True, white)
            text2 = font.render('1P Sega Rally', True, white)
            text3 = font.render('2P Daytona USA', True, green)
            text4 = font.render('2P Sega Rally', True, white)
            text10 = font.render('Quitter', True, white)
        if (selected == 3):
            text1 = font.render('1P Daytona USA', True, white)
            text2 = font.render('1P Sega Rally', True, white)
            text3 = font.render('2P Daytona USA', True, white)
            text4 = font.render('2P Sega Rally', True, green)
            text10 = font.render('Quitter', True, white)
        if (selected == 4):
            text1 = font.render('1P Daytona USA', True, white)
            text2 = font.render('1P Sega Rally', True, white)
            text3 = font.render('2P Daytona USA', True, white)
            text4 = font.render('2P Sega Rally', True, white)
            text10 = font.render('Quitter', True, green)
            
        screen.blit(text,(1920/2 - text.get_width()/ 2, 10 ))
        screen.blit(text0,(10 , 80 ))
        
        screen.blit(text1,(10 , 200 ))
        screen.blit(text2,(10 , 300 ))
        screen.blit(text3,(10 , 400 ))
        screen.blit(text4,(10 , 500 ))
        screen.blit(text10,(10 , 1000 ))

            
    
    pygame.display.flip()
    clock.tick(60)
    
    