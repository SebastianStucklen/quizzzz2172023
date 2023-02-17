
import pygame
pygame.init()
import random as rand
#screen
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("quiozz")
doExit = False
#outer
oX = 399
oY = 399
oR = 255
oG = 120
oB = 0
oRadius = 100
oThicc = 20
#inner
iX = 399
iY = 399
iR = 0
iG = 120
iB = 255
iRadius = 60
iThicc = 20
#middle
mX = 399
mY = 399
mR = 255
mG = 120
mB = 0
mRadius = 20
mThicc = 0
#scores
targetScore = 0
while not doExit:
   
#render ---------------------------------------
    #screen.fill((240,240,240))
    screen.fill((0,0,0))
    pygame.draw.circle(screen, (oR,oG,oB), (oX, oY), oRadius, oThicc)
    pygame.draw.circle(screen, (iR,iG,iB), (iX, iY), iRadius, iThicc)
    pygame.draw.circle(screen, (mR, mG, mB), (mX, mY), mRadius, mThicc)
    pygame.draw.circle(screen, (255,255,255), (399, 399), 80, 20)
    pygame.draw.circle(screen, (255,255,255), (399, 399), 40, 20)
    pygame.display.flip()
 #score
    level = int(input("What level, from 5 (outer level) to 1 (bullseye) of the target you hit"))
    if level == 1:
        print("bullseye!!!")
        print("You get a score of 50")
    elif level == 2:
        print("You get a score of 40")
    elif level == 3:
        print("You get a score of 30")
    elif level == 4:
        print("You get a score of 20")
    elif level == 5:
        print("You get a score of 10")
    else:
        print("you get no score >:(")
pygame.quit()
