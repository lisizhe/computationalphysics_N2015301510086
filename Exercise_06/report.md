# Report 06: Chaos in the Driven Nonlinear Pendlum
### Author: Li Sizhe
***
## 摘要
本次报告研究了耗散振动系统中的混沌现象，探讨了驱动力、初始相位、空气阻力对混沌系统的影响，并分别在代数空间和相空间进行了比较。

## 算法与原理
本次模拟使用了改良后的Euler-Cormer法，其改变的核心在于在迭代中使用w[i+1]代替w[i]，使得模拟结果更加精确。

主要算法如下：

* ![](http://latex.codecogs.com/gif.latex?\omega_{i+1}=\omega_{i}-[(g/l)sin{\theta_{i}}-q\omega_{i}+F_{D}sin(\Omega_{D}t_{i})]\Delta{t})
* ![](http://latex.codecogs.com/gif.latex?\theta_{i+1}=\theta_{i}+\omega_{i+1}\Delat{t})
* ![](http://latex.codecogs.com/gif.latex?t_{i+1}=t_{i}+\Delat{t})

## Python 实现

"""

for i in range(0,1500):

    W[i+1]=W[i]-((g/9.8)*math.sin(O[i])+0.5*W[i]-1.2*math.sin(2/3*t[i]))*T
    O[i+1]=O[i]+W[i+1]*T
    if O[i+1]<-math.pi:
        O[i+1]=O[i+1]+2*math.pi
    elif O[i+1]>math.pi:
        O[i+1]=O[i+1]-2*math.pi
    else:
        O[i+1]=O[i+1]
    t[i+1]=t[i]+T

"""

## 运行结果
图一
图二
图三
图四
图五
图六
## 结论
驱动力对混沌系统的影响非常显著。事实上，随着驱动力从零逐渐增大，系统逐渐由规律变为混沌系统。

空气阻力因子对混沌的影响不如驱动力明显，当其较小的时候，系统是混沌系统。随着阻力的增大，系统由混沌变为非混沌系统。

混沌系统对初始相位的改变非常敏感，而非混沌系统对初始相位的改变并不敏感。
