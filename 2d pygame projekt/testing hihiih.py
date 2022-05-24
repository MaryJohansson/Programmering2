import pygame
import random

pygame.init()

win = pygame.display.set_mode((700, 600))

# Player
playerImg = pygame.image.load('player.png')
playerX = 300
playerY = 500
playerX_change = 0

# Enemy
enemyImg = pygame.image.load('enemy.png')
enemyX = random.randint(0, 636)
enemyY = random.randint(50, 150)
enemyX_change = 0.3
enemyY_change = 0

def player(x, y):
    win.blit(playerImg, (x, y))

def enemy(x, y):
    win.blit(enemyImg, (x, y))


# Title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)
# Game Loop
running = True
while running:
    # RGB
    win.fill((0, 0, 0))

    # Running loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # If keystroke is pressed, check whether it is right or left
        if event.type == pygame.KEYDOWN:
            print("A keystroke is pressed")
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            playerX_change = 0

    playerX += playerX_change
# Boundaries of spaceship movement
    if playerX <= 0:
        playerX = 0
    elif playerX >= 636:
        playerX = 636
# Boundaries for enemy movement
    if enemyX <= 0:
        enemyX_change += 0.3
    elif enemyX >= 636:
        enemyX_change += -0.3

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()