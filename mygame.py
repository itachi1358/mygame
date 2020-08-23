#code by Arshaf

import pygame
import random
from pygame import mixer

pygame.init()
screen=pygame.display.set_mode((800,800))
title=pygame.display.set_caption("SPACE -SHOOTER")
logo =pygame.image.load("eye.png")
pygame.display.set_icon(logo)

#initiliasing everything
x=380
y=600
vel=10
height=800
width=800
run =True
enemy=[]
y1=[]
x1=[]
x1_change=[]
y1_change=[]
number_of_enemies=10
for i in range(number_of_enemies):
    x1_change.append(4)
    y1_change.append(40)
    enemy.append(pygame.image.load("skull.png"))
    y1.append(random.randint(60,100))
    x1.append(random.randint(100,780))
bulletx=380
bullety=600
bullety_change=10
bullet_state="ready"
score_value=0
font=pygame.font.Font("freesansbold.ttf",32)
txtx=10
txty=10
over=pygame.font.Font("freesansbold.ttf",64)
instr=pygame.font.Font("freesansbold.ttf",32)
instruction=instr.render("DON'T  LET ENEMIES COME NEAR YOU",True,(255,255,255))
#screen.blit(instruction,(780,10))
def game_over_text():
    over_txt=over.render("GAMEOVER",True,(255,255,255))
    screen.blit(over_txt,(300,400))
def score(x,y):
    score=font.render("SCORE:" + str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))

def collide(bx,by,x3,y3):
    distance=((bx-x3)**2 + (by-y3)**2)**0.5
    if distance <=70:
        return True
    else: 
        return False

def fire_bulet(x,y):
    bullet=pygame.image.load("torpedo.png")
    global bullet_state
    bullet_state='fire'
    screen.blit(bullet,(x+16,y))    
#the gameloop starts here
while run:
    for events in pygame.event.get():
        if events.type ==pygame.QUIT:
            run=False
    screen.fill((0,0,0))
    background=pygame.image.load("background.png")
    screen.blit(background,(0,0))
    player=pygame.image.load("ufo.png")
    screen.blit(player,(x,y))
    screen.blit(instruction,(10,50))
    k= pygame.key.get_pressed()
    if k[pygame.K_LEFT]  and x> vel:
        x -= vel
    if k[pygame.K_RIGHT] and x < 680  :
        x += vel
    if k[pygame.K_SPACE]:
        if bullet_state is "ready":
            bulletx=x
            fire_bulet(bulletx+30,bullety)
            bullety-=bullety_change    
    
    for i in range(number_of_enemies):
        if y1[i]>580:
            for j in range(number_of_enemies):
                y1[j]=2000
            game_over_text()   
        
        
        screen.blit(enemy[i],(x1[i],y1[i]))
        x1[i] += x1_change[i]
        if x1[i]<=0:
            x1_change[i]=5
            y1[i] += y1_change[i]
        elif x1[i]>=736:
            x1_change[i]=-5
            y1[i] += y1_change[i]


        collison=collide(bulletx,bullety,x1[i],y1[i])
        if collison:
            bullety=600
            bullet_state="ready"
            score_value += 1 
            y1[i]=random.randint(60,200)
            x1[i]=random.randint(100,780)   
    if bullety <=0:
        bullet_state="ready"
        bullety=600
    if bullet_state is "fire":
        fire_bulet(bulletx+30,bullety)
        bullety-=bullety_change
 
    score(txtx,txty)
    pygame.display.update()   