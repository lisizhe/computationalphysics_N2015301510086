# 第四次作业
## 程序介绍
本程序使用pygame的插件模拟物体沿抛物线运动的情况，并实现了对角度、初始速度等相关参数的调节。
## 程序代码和注释
首先我们导入pygame、sys和math库。

```
import pygame,sys,math

pygame.init()
```
接下来我们设定游戏运行的速率
```
FPS=(你想要的速度)
fpsClock=pygame.time.Clock()
```
然后绘制游戏运行窗口
```
DISPLAYS=pygame.display.set_mode((你想要的窗口大小))
pygame.display.set_caption("你想要的标题")
```
接下来定义相关变量
```
BLUE=(255,255,255)
GRAY=(192,192,192)
canon=pygame.image.load('canon.png')
bgm=pygame.image.load('bgm.jpg')
G=10
angle=math.pi/4
canonv0=110
canonvx=int(canonv0*math.cos(angle))
canonvy=int(canonv0*math.sin(angle))
canonx=10
canony=868
    
direction='up'
```
之后运行游戏主循环
```
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
    ```
