import math
import random

import pygame
from pygame import mixer
from minaklasser import *
from sys import exit
# Inviga pygame
pygame.init()

# Skapa spelplanet
skärm = pygame.display.set_mode((800, 600))
allaskott = []
# Bakgrund
bakgrund = pygame.image.load('desert1.png')

# Ljud
pygame.mixer.music.load("ljud.mp3")
pygame.mixer.music.set_volume(1.5)
mixer.music.play(-1)

# Seplets namn och Ikon
pygame.display.set_caption("Besegra Ursula")
icon = pygame.image.load('ursula.png')
pygame.display.set_icon(icon)

# Spelare
yoda = Yoda('yoda50', 440, 480)
mimmii = Mimmii('mimmii.png', 300, 480)


# Fiende
fiende = []
num_av_fiender = 10

for i in range(num_av_fiender):
    fiende.append(Fiender())



# Skott

# Ready - You can't see the bullet on the screen
# Fire - The bullet is currently moving



# Poäng
poängvärde = 0
typsnitt = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
testY = 10

# Spelet är slut
typsnitt_över = pygame.font.Font('freesansbold.ttf', 64)


def visa_poäng(x, y):
    poäng = typsnitt.render("Poäng : " + str(poängvärde), True, (255, 255, 255))
    skärm.blit(poäng, (x, y))


def spelet_slut():
    över_text = typsnitt_över.render("SPELET ÄR SLUT", True, (255, 255, 255))
    skärm.blit(över_text, (125,250))

def Knuff(fiendeX, fiendeY, skottX, skottY):
    distans = math.sqrt(math.pow(fiendeX - skottX, 2) + (math.pow(skottY - fiendeY, 2)))
    if distans < 65:
        return True
    else:
        return False

def rita(fiende):
    for skott in allaskott:
        skärm.blit(skott.bild, (skott.x, skott.y))

    for i in range(len(fiende)):
        skärm.blit(fiende[i].bild, (fiende[i].x, fiende[i].y))

    skärm.blit(yoda.bild, (yoda.x, yoda.y))
    skärm.blit(mimmii.bild, (mimmii.x, mimmii.y))

    pygame.display.update()

# När spelet är igång
igång = True
while igång:

    # RGB = Röd, Grön, Blå
    skärm.fill((0, 0, 0))
    # Bakgrunds bild
    skärm.blit(bakgrund, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            igång = False


        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                yoda.x_förändring = -5
            if event.key == pygame.K_RIGHT:
                yoda.x_förändring = 5
            if event.key == pygame.K_UP and len(allaskott) < 2:
                    skottljud = mixer.Sound("laser.wav")
                    pygame.mixer.Sound.set_volume(skottljud,0.2)
                    skottljud.play()
                    # Få x koordinat av yoda
                    skott = Skott()
                    skott.x = yoda.x
                    allaskott.append(skott)

            if event.key == pygame.K_s and len(allaskott) < 2:
                    skottljud = pygame.mixer.Sound("laser.wav")
                    pygame.mixer.Sound.set_volume(skottljud, 0.2)
                    skottljud.play()
                    # Få x koordinat av mimmi
                    skott = Skott()
                    skott.x = mimmii.x
                    allaskott.append(skott)


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                yoda.x_förändring = 0

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                mimmii.x_förändring = -5
            if event.key == pygame.K_d:
                mimmii.x_förändring = 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                mimmii.x_förändring = 0

    # 5 = 5 + -0.1 -> 5 = 5 - 0.1
    # 5 = 5 + 0.1

    yoda.x += yoda.x_förändring
    if yoda.x <= 0:
        yoda.x = 0
    elif yoda.x >= 736:
        yoda.x= 736

    mimmii.x += mimmii.x_förändring
    if mimmii.x <= 0:
        mimmii.x = 0
    elif mimmii.x >= 736:
        mimmii.x = 736

    # Fienders rörelse
    for i in range(num_av_fiender):

        # Game Over
        if fiende[i].y > 440:
            for j in range(num_av_fiender):
                fiende[j].y = 2000
            spelet_slut()
            break

        fiende[i].x += fiende[i].x_förändring
        if fiende[i].x <= 0:
            fiende[i].x_förändring = 4
            fiende[i].y += fiende[i].y_förändring
        elif fiende[i].x >= 736:
            fiende[i].x_förändring = -4
            fiende[i].y += fiende[i].y_förändring

        try:
            # Krock
            for j, skott in enumerate(allaskott):
                if Knuff(fiende[i].x, fiende[i].y, skott.x, skott.y):
                    explosion_ljud = pygame.mixer.Sound("alien.mp3")
                    pygame.mixer.Sound.set_volume(explosion_ljud, 0.2)
                    explosion_ljud.play()
                    allaskott.pop(j)
                    poängvärde += 1
                    fiende[i].x = random.randint(0, 736)
                    fiende[i].y = random.randint(50, 150)
        except:
            pass


    # Skottets rörelse
    for i, skott in enumerate(allaskott):
        skott.y -= skott.y_förändring
        if skott.y <= 0:
            allaskott.pop(i)



    visa_poäng(textX, testY)
    rita( fiende)

