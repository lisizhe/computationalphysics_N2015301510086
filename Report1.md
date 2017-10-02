# REPORT 1 
### author：lisizhe

***
## 题目表述
```
第一章第二题

The position of an object moving horizontally with a constant velocity,
V is described by the equation
dx/dt=V                       (1.9)
Assuming that the velocity is a constant,say V=40m/s,
use the Euler method to solve (1.9) for X as a function of time.
Compare your result with the exact solution.
```
## 题目的python实现
```
import matplotlib.pyplot as plt

N1=[0 for x in range(0,101)]
t1=[0 for x in range(0,101)]
N1[0]=0
T1=0.1
t1[0]=0
v=40


for i in range(1,100):
    N1[i]=N1[i-1]+v*T1
    t1[i]=i*T1


plt.title('x-t figure')
plt.xlabel('t/s')
plt.ylabel('x/m')
P1=plt.scatter(t1,N1)

plt.legend(handles = [P1], labels = ['dt=0.1s'], loc = 'best')
plt.show()
```


## 程序运行结果
![运行结果](https://github.com/lisizhe/computationalphysics_N2015301510086/blob/master/demo.png?raw=true)

## Euler 的分析介绍
```
综述

它不直接追究质点的运动过程，而是以充满运动液体质点的空间——流场为对象。
研究各时刻质点在流场中的变化规律。将个别流体质点运动过程置之不理，而固守于流场各空间点。
通过观察在流动空间中的每一个空间点上运动要素随时间的变化，把足够多的空间点综合起来而得出的整个流体的运动情况。
在数学和计算机科学中，命名自它的发明者莱昂哈德·欧拉，是一种一阶数值方法，用以对给定初值的常微分方程（即初值问题）求解。
它是一种解决数值常微分方程的最基本的一类显型方法（Explicit method）。

基本概念

欧拉法是常微分方程的数值解法的一种，其基本思想是迭代。其中分为前进的EULER法、后退的EULER法、改进的EULER法。
所谓迭代，就是逐次替代，最后求出所要求的解，并达到一定的精度。误差可以很容易地计算出来。
欧拉法是考察流体流动的一种方法，通常考察流体流动的方法有两种，即拉格朗日法和欧拉法。
欧拉法（euler method）是以流体质点流经流场中各空间点的运动即以流场作为描述对象研究流动的方法——流场法。
它不直接追究质点的运动过程，而是以充满运动液体质点的空间——流场为对象。研究各时刻质点在流场中的变化规律。
将个别流体质点运动过程置之不理，而固守于流场各空间点。通过观察在流动空间中的每一个空间点上运动要素随时间的变化，
把足够多的空间点综合起来而得出的整个流体的运动情况。在数学和计算机科学中，欧拉方法，命名自它的发明者莱昂哈德·欧拉，
是一种一阶数值方法，用以对给定初值的常微分方程（即初值问题）求解。它是一种解决数值常微分方程的最基本的一类显型方法。

```
