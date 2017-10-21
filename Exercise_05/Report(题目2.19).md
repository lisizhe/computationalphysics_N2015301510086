# REPORT 2.19
### author：lisizhe

***
## 题目描述
Model the effcet of the backspin on the range of a batted ball.Assume an angular velocity of 2000rpm.
## 题目分析
在不考虑球的空气阻力的影响时，球的运动方程表示如下：
![](http://latex.codecogs.com/gif.latex?\frac{dx}{dt}=v_x)

![](http://latex.codecogs.com/gif.latex?\frac{dy}{dt}=v_y)

![](http://latex.codecogs.com/gif.latex?\frac{dv_x}{dt}=0)

![](http://latex.codecogs.com/gif.latex?\frac{dv_y}{dt}=-g)

当我们考虑球的自旋时，有必要在微分方程中引入新的一项来描述这个变化，即V在y方向上的分量需要修正为：
![](http://latex.codecogs.com/gif.latex?\frac{dv_y}{dt}=-g-\frac{S_{0}v_{x}\omega}{m})

依据这些微分方程，我们用Euler法对球的运动情况做数值模拟。

![](http://latex.codecogs.com/gif.latex?x_i=x_{i-1}+v_x\Delta{T})

![](http://latex.codecogs.com/gif.latex?y_i=y_{i-1}+v_y\Delta{T})

![](http://latex.codecogs.com/gif.latex?v_{x,i}=v_{x,i-1}-\frac{B_2}{m}v_{i-1}v_{x,i-1}\Delta{T})

![](http://latex.codecogs.com/gif.latex?v_{y,i}=v_{y,i-1}-g\Delta{T}-\frac{S_{0}v_{x,i-1}\omega\Delta{T}}{m})

## 题目的python实现
```
import matplotlib.pyplot as plt
import math

def BACKSPIN_BALL(V0,A,U,LIM):
    
    X=[0 for x in range(0,LIM)]
    Y=[0 for x in range(0,LIM)]
    
    X[0]=0
    Y[0]=1.8
    
    T=0.01
    g=9.8

    VX=V0*math.cos(A)
    VY=V0*math.sin(A)
   
    V=V0
    for i in range(1,LIM):
        VX=VX-(0.0039*V*VX)*T
        VY=VY-g*T-(4.1*0.0001*U*VX)*T
    
        V=(VX*VX+VY*VY+VZ*VZ)**0.5
        X[i]=X[i-1]+VX*T
        Y[i]=Y[i-1]+VY*T
           
    P1=plt.plot(X,Y)
       
    return P1

BACKSPIN_BALL(15,math.pi/4,33,5001)
BACKSPIN_BALL(15,math.pi/4,-33,5001)
BACKSPIN_BALL(15,math.pi/4,0,5001)

plt.title('你需要的题目')
plt.ylabel('y/m')
plt.xlabel('x/m')
plt.xlim((0,25))
plt.ylim((0,8))

plt.show()
```

## 程序运行结果
![](https://github.com/lisizhe/computationalphysics_N2015301510086/blob/master/Exercise_05/Figure_1.png)

## 结果分析
我们可以看到上旋和下旋对球的运动有较为明显的影响。当球正旋时，球比在无旋情形下飞的更远。反之，当球逆旋时，球比在无旋情形下飞的更近。
