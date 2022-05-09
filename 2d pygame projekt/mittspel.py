import pygame
import minaklasser

pygame.init()

screen = pygame.display.set_mode((1600,900))

#Title and Icon
pygame.display.set_caption("The Mandalorian")
icon = pygame.image.load('yoda.png')
pygame.display.set_icon(icon)

#Player
playerImg = pygame.image.load('yoda.png')
playerX = 370
playerY = 480
playerX_change = 0


def draw(x,y):
    # RBG - Red, Green, Blue
    screen.fill((255, 255, 255))
    screen.blit(playerImg, (x,y))


#Game loop
running = True
while running:



    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    #if keystroke is pressed check wheter its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
            if event.key == pygame.K_LEFT:
                playerX_change = -0.1
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0.1


    # 5 = 5 + -0.1 -> 5 = 5 - 0.1.
    playerX+= playerX_change
    draw(playerX,playerY)
    pygame.display.update()