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
White=(255,255,255)
canon=pygame.image.load('duck.png') # 飞翔的鸭子
bgm=pygame.image.load('sky.jpg') # 背景图片
G=10 # 重力加速度
angle=math.pi/3 # 发射角度
canonv0=100 # 初速度
canonvx=int(canonv0*math.cos(angle))
canonvy=int(canonv0*math.sin(angle))
canonx=10 # 初始X的位置
canony=704 # 初始Y的位置
    
direction='up'
```
之后运行游戏主循环
```
while True:
    DISPLAYS.fill(White)
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
            sys.exit() # 退出程序
            
    pygame.display.update() # 刷新屏幕
    fpsClock.tick(FPS)
    ```
