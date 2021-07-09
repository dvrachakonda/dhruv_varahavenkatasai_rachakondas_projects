#a simple program that moves a red square across a screen
#this only works if you have the pygame modules installed
#to install this, enter into your command line: "pip install pygame"

#import the pygame libraries
import pygame
pygame.init()

#sets size and caption of the window
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Dhruv's game")

#variables for the square

#inital x start position
x = 50
#intial y starting position
y = 50
#width and height of the square
width = 40
heigth = 60
#rate of change when buttons are pressed to move the square
vel = 5

#while loop to keep running the program till the quit button is pressed
run = True
while run:
    pygame.time.delay(100)

    #boolean set to false to stop the while loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    #changes position through button presses
     if(keys[pygame.K_LEFT] and x != 0):
        x -= vel

    if(keys[pygame.K_RIGHT] and x != 460):
        x += vel

    if(keys[pygame.K_UP] and y != 0):
        y -= vel

    if(keys[pygame.K_DOWN] and y != 440):
        y += vel

    #fills the window, otherwise a red streak is left behind
    win.fill((0,0,0))

    pygame.draw.rect(win, (255, 0 , 0), (x, y , width, heigth))
    pygame.display.update()


pygame.quit()
