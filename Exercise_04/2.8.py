"""
Created on Wed Sep 27 08:24:57 2017

@author:lisizhe
"""
import pygame,sys,math

pygame.init()

FPS=10
fpsClock=pygame.time.Clock()

DISPLAYS=pygame.display.set_mode((1024,768))
pygame.display.set_caption("Duck is flying")

BLUE=(255,255,255)
GRAY=(192,192,192)
canon=pygame.image.load('duck.png')
bgm=pygame.image.load('sky.jpg')
G=10
angle=math.pi/3
canonv0=100
canonvx=int(canonv0*math.cos(angle))
canonvy=int(canonv0*math.sin(angle))
canonx=10
canony=704
    
direction='up'

while True:
    DISPLAYS.fill(BLUE)
    if direction=='up':
        canonx=canonx+canonvx
        canony=canony-canonvy
        canonvx=canonvx
        canonvy=canonvy-10
          
    DISPLAYS.blit(bgm,(0,0))
    DISPLAYS.blit(canon,(canonx,canony))
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    pygame.display.update()
    fpsClock.tick(FPS)